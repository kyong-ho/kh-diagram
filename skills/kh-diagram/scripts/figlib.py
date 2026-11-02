"""교육 가이드 본문 그림(SVG 도해)을 그리는 공용 모듈.

과정마다 scripts/figures/<과정>/course.py 에서 setup()으로 표제란 이름과
출력 폴더를 정하고, 그림 스크립트는 `from course import *` 로 불러 쓴다.
색·프레임·글자 크기 규칙은 docs/education-guide-style.md 의 "그림" 절.
"""
import html, os, re

# 그림 전용 색. 사이트 토큰(design/tokens.json)과는 별개다.
INK="#17406D"; TINT="#EEF3F8"; G="#23272E"; MUTE="#5A6675"; LINE="#C9D3DF"
RED="#C2362B"; REDT="#FCEDEB"; GRN="#2C7A4B"; GRNT="#EAF5EE"; AMB="#FFD978"; AMBT="#FFF6DC"
BLUE="#2F6FDE"  # 화면을 본뜬 그림의 기본 버튼
FONT="'Malgun Gothic','Apple SD Gothic Neo','Noto Sans CJK KR','Noto Sans KR',sans-serif"
COPYRIGHT="© KYONGHO ENGINEERING & ARCHITECTS"

_cfg={"course":None,"out":None}
_cur=None  # 지금 그리는 그림. 아래 도우미 함수가 여기에 그린다.

def setup(course,out):
    """course: 표제란에 적을 과정 이름. out: SVG를 쓸 폴더(FIG_OUT 환경 변수가 있으면 그쪽)."""
    _cfg["course"]=course; _cfg["out"]=os.environ.get("FIG_OUT") or out

def cur():
    """지금 그리는 그림. 과정 전용 도우미를 만들 때 쓴다."""
    return _cur

def _markers(colors,refx,size):
    return ''.join(f'<marker id="a{n}" viewBox="0 0 10 10" refX="{refx}" refY="5" markerWidth="{size}" markerHeight="{size}" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for n,c in colors)

def _strip_signature(svg):
    # 파일 전달 과정에서 붙은 서명(metadata)은 비교에서 뺀다.
    return re.sub(r'<metadata>.*?</metadata>','',svg,flags=re.S).replace(' xmlns:c2pa="http://c2pa.org/manifest"','')

class _Sheet:
    def _open(s,W,H,label):
        global _cur
        _cur=s; s.W,s.H=W,H
        s.o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}" role="img" aria-label="{html.escape(label)}">']
    def add(s,x): s.o.append(x)
    def t(s,x,y,txt,size=15,fill=G,w=400,anchor="start"):
        s.o.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{w}" text-anchor="{anchor}">{html.escape(txt)}</text>')
    def save(s,name):
        s.o.append('</svg>'); svg='\n'.join(s.o)
        os.makedirs(_cfg["out"],exist_ok=True)
        path=os.path.join(_cfg["out"],f'{name}.svg')
        # 내용이 같은 그림은 다시 쓰지 않는다(서명만 다른 파일이 바뀐 것으로 잡히지 않게).
        if os.path.exists(path) and _strip_signature(open(path,encoding='utf-8').read())==svg:
            return
        open(path,'w',encoding='utf-8').write(svg); print("쓴 그림:",path)

class S(_Sheet):
    """도면형 프레임: 화면 설명·구조·흐름 그림. 좌상단 제목, 우하단 표제란(과정 이름 | 그림 번호)."""
    def __init__(s,W,H,title,fig):
        s._open(W,H,title)
        s.o.append('<defs>'+_markers((("i",INK),("r",RED),("g",GRN),("m",MUTE)),9,7)+'</defs>')
        s.o.append(f'<rect width="{W}" height="{H}" fill="#fff"/>')
        s.o.append(f'<rect x="8" y="8" width="{W-16}" height="{H-16}" fill="none" stroke="{INK}" stroke-width="1.5"/>')
        s.t(36,52,title,23,INK,700)
        bx,by=W-8-270,H-8-30
        s.o.append(f'<g stroke="{INK}" stroke-width="1" fill="#fff"><rect x="{bx}" y="{by}" width="190" height="30"/><rect x="{bx+190}" y="{by}" width="80" height="30"/></g>')
        s.t(bx+10,by+20,_cfg["course"],12,INK); s.t(bx+200,by+20,fig,12,INK)
        s.t(18,H-17,COPYRIGHT,10,"#8A96A5")
    def r(s,x,y,w,h,fill="#fff",stroke=INK,rx=4,sw=1.5,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        s.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def p(s,d,c="i",dash=None,sw=2):
        """화살표. c는 색(i 남색, r 빨강, g 초록, m 회색)."""
        col={"i":INK,"r":RED,"g":GRN,"m":MUTE}[c]; ds=f' stroke-dasharray="{dash}"' if dash else ''
        s.o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" marker-end="url(#a{c})"{ds}/>')
    def b(s,x,y,n,fill=INK):
        """번호 원."""
        s.o.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{fill}"/>'); s.t(x,y+5,str(n),14,"#fff",700,"middle")
    def box(s,x,y,w,h,title,sub=None,fill="#fff",stroke=INK,tc=G,dash=None):
        s.r(x,y,w,h,fill,stroke,dash=dash)
        if sub: s.t(x+16,y+h/2-3,title,16,tc,700); s.t(x+16,y+h/2+17,sub,12.5,MUTE)
        else: s.t(x+16,y+h/2+6,title,16,tc,700)

class P(_Sheet):
    """개념 만화형 프레임: 비유로 개념을 소개하는 그림. 좌상단 번호 원, 아래 띠에 제목과 한 줄 설명."""
    def __init__(s,n,cap,sub,W=960,H=480):
        s._open(W,H,cap)
        s.o+=[f'<defs><clipPath id="c"><rect x="4" y="4" width="{W-8}" height="{H-8}" rx="18"/></clipPath>'+_markers((("i",INK),("r",RED),("g",GRN)),8,6)+'</defs>',
        f'<rect width="{W}" height="{H}" fill="#fff"/>',f'<g clip-path="url(#c)"><rect x="0" y="{H-96}" width="{W}" height="96" fill="{TINT}"/></g>',
        f'<rect x="4" y="4" width="{W-8}" height="{H-8}" rx="18" fill="none" stroke="{INK}" stroke-width="2.5"/>']
        s.o.append(f'<circle cx="46" cy="46" r="21" fill="{INK}"/>'); s.t(46,53,str(n),19,"#fff",700,"middle")
        s.t(40,H-54,cap,23,INK,700); s.t(40,H-24,sub,15.5,MUTE)
        s.t(W-22,27,COPYRIGHT,10,"#8A96A5",400,"end")
    def arrow(s,d,c="i",dash=None,sw=3.5):
        col={"i":INK,"r":RED,"g":GRN}[c]; ds=f' stroke-dasharray="{dash}"' if dash else ''
        s.o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#a{c})"{ds}/>')
    def person(s,x,y,mood="smile",k=1.0,color=INK,label=None):
        """사람. mood: smile, sad, flat, 그 밖의 값은 놀란 입."""
        m={"smile":"M-9,9 Q0,18 9,9","sad":"M-9,15 Q0,7 9,15","flat":"M-8,12 H8"}.get(mood)
        mouth=f'<path d="{m}" fill="none" stroke="{G}" stroke-width="2.5" stroke-linecap="round"/>' if m else f'<circle cx="0" cy="12" r="4.5" fill="{G}"/>'
        s.o.append(f'<g transform="translate({x},{y}) scale({k})"><path d="M-36,104 Q-36,36 0,36 Q36,36 36,104 Z" fill="{color}"/><circle r="29" fill="#fff" stroke="{color}" stroke-width="3"/><circle cx="-10" cy="-3" r="3" fill="{G}"/><circle cx="10" cy="-3" r="3" fill="{G}"/>{mouth}</g>')
        if label: s.t(x,y+104*k+22,label,14,MUTE,700,"middle")
    def robot(s,x,y,k=1.0,label="AI"):
        s.o.append(f'<g transform="translate({x},{y}) scale({k})"><line x1="0" y1="-26" x2="0" y2="-40" stroke="{INK}" stroke-width="3"/><circle cx="0" cy="-44" r="5" fill="{RED}"/><rect x="-24" y="30" width="48" height="40" rx="10" fill="{INK}"/><rect x="-32" y="-26" width="64" height="52" rx="14" fill="#fff" stroke="{INK}" stroke-width="3"/><circle cx="-13" cy="-3" r="6" fill="{GRN}"/><circle cx="13" cy="-3" r="6" fill="{GRN}"/><path d="M-9,13 H9" stroke="{G}" stroke-width="2.5" stroke-linecap="round"/></g>')
        if label: s.t(x,y+70*k+22,label,14,MUTE,700,"middle")
    def doc(s,x,y,w=64,h=80,rot=0,label=None,broken=False,diff=False):
        """문서 한 장. broken은 빨간 X, diff는 바뀐 줄 표시."""
        cx,cy=x+w/2,y+h/2; ln=""
        for i in range(4):
            yy=y+24+i*13; col=LINE
            if diff: col=[GRN,LINE,RED,GRN][i]
            ln+=f'<line x1="{x+10}" y1="{yy}" x2="{x+w-(10 if i%2 else 20)}" y2="{yy}" stroke="{col}" stroke-width="{4 if diff else 3}" stroke-linecap="round"/>'
        br=f'<path d="M{x+8},{y+12} L{x+w-8},{y+h-10} M{x+w-8},{y+12} L{x+8},{y+h-10}" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>' if broken else ""
        s.o.append(f'<g transform="rotate({rot} {cx} {cy})"><path d="M{x},{y} h{w-16} l16,16 v{h-16} h{-w} z" fill="#fff" stroke="{RED if broken else INK}" stroke-width="2.5" stroke-linejoin="round"/><path d="M{x+w-16},{y} v16 h16" fill="none" stroke="{RED if broken else INK}" stroke-width="2.5" stroke-linejoin="round"/>{ln}{br}</g>')
        if label: s.t(cx,y+h+24,label,13,G,400,"middle")
    def pc(s,x,y,w,h,fill="#fff"):
        s.o.append(f'<rect x="{x+w/2-22}" y="{y+h}" width="44" height="20" fill="{INK}"/><rect x="{x+w/2-60}" y="{y+h+18}" width="120" height="9" rx="4.5" fill="{INK}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{INK}" stroke-width="3.5"/>')
    def cloud(s,cx,cy,k=1.0,label=""):
        sh=[(-55,12,34),(-12,-14,46),(40,0,37),(72,20,26)]
        a=''.join(f'<circle cx="{x}" cy="{y}" r="{r+3}" fill="{GRN}"/>' for x,y,r in sh)+f'<rect x="-55" y="12" width="127" height="37" fill="{GRN}"/>'
        b=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{GRNT}"/>' for x,y,r in sh)+f'<rect x="-55" y="12" width="127" height="34" fill="{GRNT}"/>'
        s.o.append(f'<g transform="translate({cx},{cy}) scale({k})">{a}{b}<text x="8" y="18" font-size="21" font-weight="700" fill="{GRN}" text-anchor="middle">{label}</text></g>')
    def stamp(s,x,y,txt,r=40,rot=-12,size=15):
        s.o.append(f'<g transform="rotate({rot} {x} {y})"><circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{RED}" stroke-width="4"/><circle cx="{x}" cy="{y}" r="{r-6}" fill="none" stroke="{RED}" stroke-width="1.5"/><text x="{x}" y="{y+size*0.36}" font-size="{size}" font-weight="700" fill="{RED}" text-anchor="middle">{txt}</text></g>')
    def bubble(s,x,y,w,h,lines,tip,size=15.5):
        """말풍선. lines는 줄 목록, tip은 꼬리가 가리킬 좌표."""
        ax=min(max(tip[0],x+30),x+w-30); by=y+h if tip[1]>y+h else y
        if tip[0]<x: a,b=(x,y+h/2-10),(x,y+h/2+10)
        elif tip[0]>x+w: a,b=(x+w,y+h/2-10),(x+w,y+h/2+10)
        else: a,b=(ax-11,by),(ax+11,by)
        s.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#fff" stroke="{INK}" stroke-width="2.5"/><path d="M{a[0]},{a[1]} L{tip[0]},{tip[1]} L{b[0]},{b[1]}" fill="#fff" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/><line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#fff" stroke-width="4"/>')
        y0=y+h/2-(len(lines)-1)*11+5.5
        for i,l in enumerate(lines): s.t(x+w/2,y0+i*22,l,size,G,700,"middle")
    def dots(s,x1,x2,y,pts,color=INK,sw=5):
        """가로줄 위에 점을 찍은 시간 흐름. pts는 (x, 색) 목록."""
        s.o.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>')
        for x,c in pts: s.o.append(f'<circle cx="{x}" cy="{y}" r="13" fill="#fff" stroke="{c}" stroke-width="5"/>')
    def lock(s,x,y,c=GRN):
        s.o.append(f'<path d="M{x-10},{y-4} v-9 a10,10 0 0 1 20,0 v9" fill="none" stroke="{c}" stroke-width="4"/><rect x="{x-16}" y="{y-5}" width="32" height="26" rx="5" fill="{c}"/>')

# ============ 도면형(S) 그림 도우미: 지금 그리는 그림에 그린다 ============
def callout(n,x,y):
    """화면 위에 얹는 빨간 번호 원(흰 테)."""
    s=_cur; s.o.append(f'<circle cx="{x}" cy="{y}" r="15" fill="#fff"/>'); s.b(x,y,n,RED)
def legend(items,x=None,y0=None,gap=None):
    """오른쪽 세로 범례. items는 (제목, 설명) 목록, 설명의 줄바꿈은 \\n."""
    s=_cur; x = 610 if x is None else x; y0 = 118 if y0 is None else y0; gap = 92 if gap is None else gap
    for i,(a,b_) in enumerate(items):
        y=y0+i*gap; s.b(x,y,i+1,RED); s.t(x+26,y+6,a,15,G,700)
        for j,line in enumerate(b_.split("\n")): s.t(x+26,y+30+j*19,line,12.5,MUTE)
def legend_row(items,y,cols=3,w=None):
    """아래쪽 가로 범례."""
    s=_cur; w = w or (880//cols)
    for i,(a,b_) in enumerate(items):
        cx=40+(i%cols)*w; cy=y+(i//cols)*54
        s.b(cx+12,cy,i+1,RED); s.t(cx+34,cy+5,a,13.5,G,700); s.t(cx+34,cy+26,b_,12,MUTE)
def note(y,txt="실제 화면을 단순하게 그린 그림입니다. 버전에 따라 모양과 위치가 조금 다를 수 있습니다."):
    _cur.t(40,y,txt,12.5,MUTE)
def appwin(x,y,w,h,title=None):
    """프로그램 창 또는 대화 상자."""
    s=_cur; s.r(x,y,w,h,"#fff",G,rx=8)
    if title:
        s.t(x+20,y+34,title,15.5,G,700)
        s.o.append(f'<line x1="{x}" y1="{y+52}" x2="{x+w}" y2="{y+52}" stroke="{LINE}"/>')
def browser(x,y,w,h,url):
    s=_cur; s.r(x,y,w,h,"#fff",G,rx=8); s.r(x,y,w,40,"#ECEFF3",G,rx=8); s.o.append(f'<rect x="{x+1}" y="{y+26}" width="{w-2}" height="14" fill="#ECEFF3"/>')
    s.o.append(f'<line x1="{x}" y1="{y+40}" x2="{x+w}" y2="{y+40}" stroke="{G}" stroke-width="1.5"/>')
    s.r(x+16,y+9,w-32,22,"#fff",LINE,rx=11,sw=1); s.t(x+30,y+25,url,12,MUTE)
def field(x,y,w,label,val,btn=None,bw=86):
    """입력 칸. btn을 주면 오른쪽에 붙는 버튼."""
    s=_cur
    if label: s.t(x,y,label,13,G,700)
    s.r(x,y+8,w,32,"#fff",LINE,rx=4,sw=1.5); s.t(x+10,y+29,val,13.5,G if val else "#9AA5B1")
    if btn: s.r(x+w+8,y+8,bw,32,"#F3F5F8",LINE,rx=4,sw=1.5); s.t(x+w+8+bw/2,y+29,btn,13,G,400,"middle")
def button(x,y,w,label,primary=True,h=34,fill=None):
    s=_cur; f = fill or (BLUE if primary else "#fff")
    s.r(x,y,w,h,f,f if primary else LINE,rx=5); s.t(x+w/2,y+h/2+5,label,13.5,"#fff" if primary else G,700 if primary else 400,"middle")
def check(x,y,label,on=True):
    s=_cur; s.r(x,y,18,18,INK if on else "#fff",INK,rx=3)
    if on: s.t(x+3,y+14,"✓",13,"#fff",700)
    s.t(x+28,y+14,label,13.5,G)
def radio(x,y,label,on=False):
    s=_cur; s.o.append(f'<circle cx="{x+9}" cy="{y+9}" r="8.5" fill="#fff" stroke="{INK}" stroke-width="1.8"/>')
    if on: s.o.append(f'<circle cx="{x+9}" cy="{y+9}" r="4.5" fill="{INK}"/>')
    s.t(x+26,y+14,label,13.5,G)
def panel(x,y,w,h,n,title):
    """번호와 제목이 붙은 칸. 한 그림을 여러 단계로 나눌 때."""
    s=_cur; s.r(x,y,w,h,"#fff",LINE,rx=10,sw=2); s.b(x+24,y+26,n); s.t(x+46,y+32,title,14.5,G,700)
def appicon(x,y,label):
    s=_cur; s.o.append(f'<rect x="{x}" y="{y}" width="72" height="72" rx="17" fill="{INK}"/><rect x="{x+18}" y="{y+18}" width="36" height="36" rx="6" fill="#fff"/><path d="M{x+26},{y+36} h20 M{x+36},{y+26} v20" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    s.t(x+36,y+96,label,12.5,G,700,"middle")
def dropdown(x,y,w,items,hl=None,header=None):
    """펼친 메뉴. hl은 강조할 항목 순번, header는 위쪽 검색 칸 문구. 높이를 돌려준다."""
    s=_cur; h=len(items)*32+(40 if header else 12)
    s.r(x,y,w,h,"#fff",G,rx=6)
    yy=y+8
    if header:
        s.r(x+10,y+8,w-20,28,"#fff",LINE,rx=4,sw=1); s.t(x+20,y+27,header,12,"#9AA5B1"); yy=y+44
    for i,t in enumerate(items):
        if hl==i: s.r(x+4,yy-2,w-8,28,"#DCE3EC","#DCE3EC",rx=4)
        s.t(x+16,yy+17,t,12.5,G,700 if hl==i else 400); yy+=32
    return h
def diffline(x,y,w,text,kind):
    """바뀐 줄 한 줄. kind는 "+"(추가), "-"(삭제), " "(그대로)."""
    s=_cur; fill={"+":"#E6F6EA","-":"#FCE9E7"," ":"#fff"}[kind]; col={"+":"#1F5F36","-":"#9B2C22"," ":G}[kind]
    s.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="26" fill="{fill}"/>'); s.t(x+10,y+18,(kind if kind!=" " else " ")+"  "+text,13,col)
def caret(x,y,col):
    _cur.o.append(f'<path d="M{x},{y} l8,0 l-4,5 z" fill="{col}"/>')
def lane(y,col,name):
    """흐름 줄 왼쪽의 이름표."""
    s=_cur; s.o.append(f'<path d="M{52},{y-15} h70 a6,6 0 0 1 6,6 v18 a6,6 0 0 1 -6,6 h-70 l-12,-15 z" fill="#fff" stroke="{col}" stroke-width="2"/>')
    s.t(92,y+5,name,15,col,700,"middle")
def dot(x,y,col,filled=False):
    _cur.o.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{col if filled else "#fff"}" stroke="{col}" stroke-width="4"/>')
