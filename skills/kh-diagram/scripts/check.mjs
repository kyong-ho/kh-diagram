// figlib.py로 만든 SVG 그림을 브라우저로 그려 PNG로 남기고, 글자 넘침·겹침을 찾는다.
// 사용: node scripts/figures/check.mjs <SVG 파일 또는 폴더...> [--out <PNG 폴더>]
// 찾는 것: 테두리 밖으로 나간 글자, 서로 겹친 글자, 상자 경계에 걸친 글자, 글자를 지나는 선·화살표.
// 글자 폭은 실제 글꼴로 잰다. 찾은 것은 후보이므로 PNG를 열어 눈으로 확인한 뒤 고친다.
import { chromium } from '@playwright/test';
import { mkdir, readdir, stat } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const outAt = args.indexOf('--out');
const outDir = outAt >= 0 ? args.splice(outAt, 2)[1] : path.join(os.tmpdir(), 'kh-diagram-check');
if (!args.length) {
  console.error('사용: node scripts/figures/check.mjs <SVG 파일 또는 폴더...> [--out <PNG 폴더>]');
  process.exit(2);
}

const files = [];
for (const arg of args) {
  if ((await stat(arg)).isDirectory()) {
    for (const name of (await readdir(arg)).sort()) if (name.endsWith('.svg')) files.push(path.join(arg, name));
  } else files.push(arg);
}
await mkdir(outDir, { recursive: true });

// 브라우저 안에서 실행한다. 좌표는 모두 화면 좌표(getBoundingClientRect)로 비교한다.
function inspect() {
  const svg = document.querySelector('svg');
  const W = svg.viewBox.baseVal.width, H = svg.viewBox.baseVal.height;
  const skip = (el) => el.closest('defs, marker, clipPath');
  const box = (el) => { const r = el.getBoundingClientRect(); return { x1: r.left, y1: r.top, x2: r.right, y2: r.bottom }; };
  const shrink = (b, d) => ({ x1: b.x1 + d, y1: b.y1 + d, x2: b.x2 - d, y2: b.y2 - d });
  const meets = (a, b) => a.x1 < b.x2 && b.x1 < a.x2 && a.y1 < b.y2 && b.y1 < a.y2;
  const inside = (a, b) => a.x1 >= b.x1 && a.x2 <= b.x2 && a.y1 >= b.y1 && a.y2 <= b.y2;
  const all = [...svg.querySelectorAll('text')].filter((t) => !skip(t) && t.textContent.trim())
    .map((t) => ({ el: t, label: t.textContent.trim().slice(0, 30), b: shrink(box(t), 1.5) }));
  // 번호 원(b, callout) 안의 숫자는 일부러 상자 모서리·선 위에 얹으므로 상자·선 검사에서 뺀다.
  const circles = [...svg.querySelectorAll('circle')].filter((c) => !skip(c)).map(box);
  const badge = (t) => circles.some((c) => inside(t.b, c));
  // 나중에 그린 칠한 사각형(펼친 메뉴, 덮어쓴 탭)에 가려진 부분은 보이지 않으므로 문제로 치지 않는다.
  const fills = [...svg.querySelectorAll('rect')].filter((r) => !skip(r) && getComputedStyle(r).fill !== 'none').map((el) => ({ el, b: box(el) }));
  const after = (a, b) => b.compareDocumentPosition(a) & Node.DOCUMENT_POSITION_FOLLOWING;
  const hidden = (b, el) => fills.some((f) => f.el !== el && after(f.el, el) && inside(b, f.b));
  const texts = all.filter((t) => !hidden(t.b, t.el));
  const problems = [];
  const frame = { x1: 8, y1: 8, x2: W - 8, y2: H - 8 };
  for (const t of texts) if (!inside(t.b, frame)) problems.push(`테두리 밖: "${t.label}"`);
  for (let i = 0; i < texts.length; i++)
    for (let j = i + 1; j < texts.length; j++)
      if (meets(texts[i].b, texts[j].b)) problems.push(`글자끼리 겹침: "${texts[i].label}" / "${texts[j].label}"`);
  // 상자: 글자와 일부만 겹치면 경계에 걸친 것이다. 그림 전체를 덮는 바탕·테두리와,
  // 둥근 모서리를 메우는 테두리 없는 덧칠(appwin 머리, desktop 위 띠)은 뺀다.
  const rects = [...svg.querySelectorAll('rect')].filter((r) => !skip(r) && getComputedStyle(r).stroke !== 'none')
    .map((r) => ({ el: r, b: box(r) })).filter(({ b }) => b.x2 - b.x1 < W - 20 || b.y2 - b.y1 < H - 20);
  for (const t of texts.filter((x) => !badge(x)))
    for (const r of rects)
      if (meets(t.b, r.b) && !inside(t.b, r.b) && !inside(r.b, t.b) && !hidden(t.b, r.el)) {
        problems.push(`상자 경계에 걸침: "${t.label}"`);
        break;
      }
  // 선·화살표: 선 위의 점이 글자 영역 안에 들어오면 겹친 것이다.
  const lines = [...svg.querySelectorAll('path, line, polyline')].filter((p) => !skip(p) && getComputedStyle(p).stroke !== 'none');
  for (const p of lines) {
    const len = p.getTotalLength(), m = p.getScreenCTM();
    const pts = [];
    for (let d = 0; d <= len; d += 2) {
      const q = p.getPointAtLength(d).matrixTransform(m);
      if (!hidden({ x1: q.x, y1: q.y, x2: q.x, y2: q.y }, p)) pts.push(q);
    }
    for (const t of texts) {
      if (badge(t)) continue;
      if (t.el.parentNode === p.parentNode && p.parentNode !== svg) continue; // 같은 부품 안(예: 구름 글자)
      if (pts.some((q) => q.x > t.b.x1 && q.x < t.b.x2 && q.y > t.b.y1 && q.y < t.b.y2))
        problems.push(`선이 글자를 지남: "${t.label}"`);
    }
  }
  return { W, H, problems: [...new Set(problems)] };
}

const browser = await chromium.launch();
let total = 0;
try {
  for (const file of files) {
    const page = await browser.newPage({ viewport: { width: 400, height: 300 }, deviceScaleFactor: 2 });
    await page.goto(pathToFileURL(path.resolve(file)).href);
    await page.evaluate(() => document.fonts.ready);
    const size = await page.evaluate(() => { const v = document.querySelector('svg').viewBox.baseVal; return { width: Math.ceil(v.width), height: Math.ceil(v.height) }; });
    await page.setViewportSize(size);
    const { problems } = await page.evaluate(inspect);
    // 과정마다 같은 이름(1-01.svg)이 있으므로 폴더 이름을 앞에 붙인다.
    const png = path.join(outDir, `${path.basename(path.dirname(path.resolve(file)))}-${path.basename(file, '.svg')}.png`);
    await page.screenshot({ path: png });
    await page.close();
    total += problems.length;
    console.log(`${problems.length ? '확인 필요' : '이상 없음'}  ${file}  →  ${png}`);
    for (const p of problems) console.log(`    - ${p}`);
  }
} finally {
  await browser.close();
}
console.log(total ? `\n후보 ${total}건. PNG를 열어 실제로 넘치거나 겹쳤는지 확인하세요.` : '\n모든 그림 이상 없음.');
process.exitCode = total ? 1 : 0;
