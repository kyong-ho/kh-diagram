"""예시 그림을 이 스킬의 figlib.py로 다시 만들어 references/reference-svg/ 의 기준 그림과 같은지 확인한다.

    python3 <스킬 폴더>/scripts/verify_examples.py [figlib.py 경로]

경로를 주면 그 figlib.py(예: 프로젝트에 복사해 둔 것)로 확인한다. 결과는 임시 폴더에만 쓴다.
"""
import glob, os, re, shutil, subprocess, sys, tempfile

HERE=os.path.dirname(os.path.abspath(__file__))
SKILL=os.path.dirname(HERE)
figlib=os.path.abspath(sys.argv[1]) if len(sys.argv)>1 else os.path.join(HERE,'figlib.py')
strip=lambda svg: re.sub(r'<metadata>.*?</metadata>','',svg,flags=re.S).replace(' xmlns:c2pa="http://c2pa.org/manifest"','')
bad=total=0
with tempfile.TemporaryDirectory() as tmp:
    # 예시 course.py는 ../../../scripts 에서 figlib를 찾으므로 같은 모양으로 임시 폴더를 꾸린다.
    os.makedirs(os.path.join(tmp,'scripts')); shutil.copy(figlib,os.path.join(tmp,'scripts','figlib.py'))
    shutil.copytree(os.path.join(SKILL,'references','examples'),os.path.join(tmp,'references','examples'))
    for course in sorted(os.listdir(os.path.join(tmp,'references','examples'))):
        out=os.path.join(tmp,'out',course)
        subprocess.run([sys.executable,os.path.join(HERE,'build.py'),os.path.join(tmp,'references','examples',course)],env={**os.environ,'FIG_OUT':out},check=True,stdout=subprocess.DEVNULL)
        for ref in sorted(glob.glob(os.path.join(SKILL,'references','reference-svg',course,'*.svg'))):
            total+=1; name=os.path.basename(ref); got=os.path.join(out,name)
            if not os.path.exists(got): print('없음  ',course,name); bad+=1; continue
            if strip(open(ref,encoding='utf-8').read())!=open(got,encoding='utf-8').read(): print('다름  ',course,name); bad+=1
print(f'기준 그림 {total}장 중 {total-bad}장 같음.' if bad else f'기준 그림 {total}장 모두 같음.')
sys.exit(1 if bad else 0)
