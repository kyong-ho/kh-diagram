# GitHub 기초 가이드 3~5장 그림.
from course import *

# ============ 3장: 계정 ============
s=S(960,420,"준비는 세 장에 나눠 진행합니다","그림 3-1")
parts=[("3장","GitHub 계정 준비","가입, 2단계 인증","웹 브라우저에서 · OS 무관","약 15분",INK,"#fff"),
       ("4장","프로그램 설치","VS Code, GitHub Desktop","Windows와 Mac이 다름","약 20분",INK,"#fff"),
       ("5장","첫 저장소 만들기","만들고, GitHub에 올리고, 확인","Windows와 Mac이 조금 다름","약 10분",GRN,GRNT)]
for i,(no,t,a,b_,c,col,fl) in enumerate(parts):
    x=40+i*300
    s.r(x,90,270,230,fl,col); s.t(x+22,126,no,14,col,700); s.t(x+22,158,t,19,G,700)
    s.t(x+22,196,a,13.5,MUTE); s.o.append(f'<line x1="{x+22}" y1="214" x2="{x+248}" y2="214" stroke="{LINE}"/>')
    s.t(x+22,242,b_,13.5,G); s.t(x+22,290,c,14,col,700)
    if i<2: s.p(f"M{x+272},205 L{x+298},205")
s.t(40,370,"한 장이 끝날 때마다 쉬어도 됩니다. 각 장 끝의 확인 목록이 모두 체크되면 다음 장으로 넘어갑니다.",13.5,MUTE)
s.save("3-01")

s=S(960,600,"GitHub 가입 화면에서 채울 곳","그림 3-2")
browser(40,84,520,420,"github.com/signup")
s.t(80,170,"Sign up for GitHub",20,G,700)
field(80,210,440,"Email","hong@example.com")
field(80,272,440,"Password","••••••••••")
field(80,334,440,"Username","gildong-hong")
button(80,404,440,"Continue",h=38,fill="#1F883D")
for n,(cx,cy) in enumerate([(528,234),(528,296),(528,358),(528,423)],1): callout(n,cx,cy)
legend([("이메일","인증 번호를 받을 수 있는 주소"),("비밀번호","다른 사이트와 겹치지 않게"),("사용자 이름","영문·숫자·하이픈. 저장소 주소에 들어갑니다\n예: gildong-hong"),("다음으로","이메일로 온 인증 번호를 입력하면 끝")])
note(540,"가입 화면의 배치는 GitHub 사정에 따라 자주 바뀝니다. 칸 이름(Email, Password, Username)을 보고 채우세요.")
s.save("3-02")

s=S(960,680,"2단계 인증은 네 단계로 켭니다","그림 3-3")
W2,H2=430,240
P=[(40,84),(490,84),(40,344),(490,344)]
panel(*P[0],W2,H2,1,"프로필 사진 → Settings")
x,y=P[0]
s.o.append(f'<circle cx="{x+390}" cy="{y+70}" r="16" fill="#C9D3DF"/>'); s.p(f"M{x+390},{y+90} L{x+390},{y+104}","m",sw=1.5)
s.r(x+230,y+108,180,112,"#fff",LINE,rx=6,sw=1.5)
for i,t in enumerate(["Your profile","Your repositories","Settings","Sign out"]):
    if t=="Settings": s.r(x+234,y+112+i*26,172,24,"#DCE3EC","#DCE3EC",rx=4)
    s.t(x+246,y+129+i*26,t,12.5,G,700 if t=="Settings" else 400)
s.t(x+24,y+90,"GitHub 오른쪽 위의",13,MUTE); s.t(x+24,y+110,"프로필 사진을 누릅니다",13,MUTE)
panel(*P[1],W2,H2,2,"Password and authentication")
x,y=P[1]
s.r(x+20,y+60,150,160,"#F5F6F8",LINE,rx=6,sw=1)
for i,t in enumerate(["Public profile","Account","Emails"]): s.t(x+32,y+86+i*22,t,12,G)
s.r(x+24,y+146,142,46,"#DCE3EC","#DCE3EC",rx=4); s.t(x+32,y+165,"Password and",12,G,700); s.t(x+32,y+183,"authentication",12,G,700)
s.r(x+184,y+116,232,40,"#1F883D","#1F883D",rx=5); s.t(x+300,y+141,"Enable two-factor authentication",12,"#fff",700,"middle")
s.t(x+184,y+100,"왼쪽 메뉴를 고르고 누릅니다",12.5,MUTE)
panel(*P[2],W2,H2,3,"QR 코드 찍고 6자리 입력")
x,y=P[2]
s.r(x+30,y+64,120,120,"#fff",G,rx=4)
import random
random.seed(3)
for i in range(10):
    for j in range(10):
        if random.random()<0.45 or (i<3 and j<3) or (i>6 and j<3) or (i<3 and j>6):
            s.o.append(f'<rect x="{x+36+i*10.8}" y="{y+70+j*10.8}" width="10.8" height="10.8" fill="{G}"/>')
s.r(x+180,y+64,70,120,"#fff",INK,rx=12,sw=2.5); s.t(x+215,y+124,"123 456",12,INK,700,"middle"); s.t(x+215,y+200,"인증 앱",12,MUTE,700,"middle")
s.p(f"M{x+160},{y+124} L{x+176},{y+124}","i",sw=2)
field(x+270,y+96,140,"","123456")
s.t(x+270,y+90,"숫자 입력",12.5,MUTE,700)
panel(*P[3],W2,H2,4,"복구 코드 내려받아 보관")
x,y=P[3]
s.r(x+30,y+62,220,120,"#F5F6F8",LINE,rx=6,sw=1)
for i in range(4): s.t(x+48,y+90+i*24,"xxxxx-xxxxx",13,MUTE,400)
button(x+270,y+100,130,"Download",primary=False)
s.t(x+30,y+210,"휴대폰을 잃어버렸을 때 로그인하는 유일한 수단입니다",12.5,RED,700)
s.t(40,616,"QR 코드와 복구 코드는 예시입니다. 실제 값은 다른 사람에게 보여 주거나 캡처해서 공유하지 않습니다.",12.5,MUTE)
s.save("3-03")

# ============ 4장: 설치 ============
s=S(960,470,"Windows: 설치 파일을 실행하고 다음을 누릅니다","그림 4-1")
steps=[("사용권 계약","동의합니다",None),("추가 작업 선택","기본값 그대로","다음"),("설치 준비 완료","","설치"),("설치 완료","","마침")]
for i,(t,sub,btn) in enumerate(steps):
    x=40+i*225; y=90
    s.r(x,y,205,230,"#fff",G,rx=6); s.r(x,y,205,30,"#E9EDF2",G,rx=6); s.o.append(f'<rect x="{x+1}" y="{y+18}" width="203" height="12" fill="#E9EDF2"/>')
    s.t(x+12,y+21,"설치 프로그램",11.5,MUTE,700)
    s.t(x+14,y+58,t,14,G,700)
    if i==0: radio(x+14,y+86,"동의합니다",True); radio(x+14,y+114,"동의하지 않습니다",False)
    if i==1:
        for j in range(4): check(x+14,y+74+j*24,["바탕 화면 아이콘","탐색기 메뉴 추가","연결 프로그램 등록","PATH에 추가"][j],j==3)
    if i==2: s.t(x+14,y+96,"설정한 내용으로",12.5,MUTE); s.t(x+14,y+116,"설치를 시작합니다",12.5,MUTE)
    if i==3: s.t(x+14,y+96,"설치가 끝났습니다",12.5,MUTE)
    lab = btn or "다음"
    button(x+105,y+186,86,lab,h=32)
    callout(i+1,x+191,y+202)
    if i<3: s.p(f"M{x+207},{y+115} L{x+223},{y+115}")
s.t(40,370,"① 동의 → ② 체크는 바꾸지 않고 다음 → ③ 설치 → ④ 마침. 화면 수와 체크 항목 이름은 프로그램마다 조금 다릅니다.",13.5,G)
s.t(40,396,"GitHub Desktop은 이런 선택 화면 없이 설치 파일을 실행하면 바로 설치되고 열립니다.",13.5,MUTE)
note(430)
s.save("4-01-win")

s=S(960,500,"Mac: 압축을 풀고 응용 프로그램 폴더로 끌어 놓습니다","그림 4-1")
X,Y=40,84
s.r(X,Y,880,300,"#fff",G,rx=8); s.r(X,Y,880,34,"#ECEFF3",G,rx=8); s.o.append(f'<rect x="{X+1}" y="{Y+22}" width="878" height="12" fill="#ECEFF3"/>')
for i,c in enumerate(["#FF5F57","#FEBC2E","#28C840"]): s.o.append(f'<circle cx="{X+18+i*18}" cy="{Y+17}" r="6" fill="{c}"/>')
s.t(X+440,Y+23,"다운로드",13,G,700,"middle")
s.o.append(f'<rect x="{X+1}" y="{Y+34}" width="169" height="265" fill="#F5F6F8"/><line x1="{X+170}" y1="{Y+34}" x2="{X+170}" y2="{Y+300}" stroke="{LINE}"/>')
s.t(X+16,Y+62,"즐겨찾기",11.5,MUTE,700)
for i,(t,hl) in enumerate([("다운로드",True),("응용 프로그램",False),("데스크탑",False),("문서",False)]):
    yy=Y+80+i*34
    if hl: s.r(X+8,yy-4,154,28,"#DCE3EC","#DCE3EC",rx=5)
    s.t(X+22,yy+15,t,13.5,G,700 if i==1 else 400)
s.r(X+14,Y+110,146,30,"none",RED,rx=6,sw=2.5,dash="5 4")
s.r(X+230,Y+80,70,84,"#E9EDF2","#9AA5B1",rx=6); s.t(X+265,Y+130,"ZIP",14,MUTE,700,"middle"); s.t(X+265,Y+188,"받은 파일.zip",11.5,G,400,"middle")
s.p(f"M{X+312},{Y+122} L{X+372},{Y+122}","i",sw=2.5); s.t(X+342,Y+110,"더블클릭",12,INK,700,"middle")
appicon(X+392,Y+86,"앱 (VS Code 등)")
s.p(f"M{X+400},{Y+204} C {X+330},{Y+285} {X+220},{Y+255} {X+168},{Y+130}","r",dash="7 5",sw=3)
s.t(X+330,Y+284,"응용 프로그램으로 끌어 놓기",14,RED,700,"middle")
for i,(a,b_) in enumerate([("zip 파일 더블클릭","압축이 풀리며 앱이 나타납니다"),("응용 프로그램으로 끌어 놓기","왼쪽 목록의 응용 프로그램 위에 놓습니다"),("응용 프로그램에서 실행","처음 실행 경고에는 열기")]):
    y=Y+70+i*72; s.b(X+560,y,i+1,RED if i==1 else INK); s.t(X+586,y+6,a,15,G,700); s.t(X+586,y+28,b_,12.5,MUTE)
s.t(40,420,"VS Code와 GitHub Desktop 모두 같은 방법으로 설치합니다.",13.5,G)
note(444)
s.save("4-01-mac")

s=S(960,630,"GitHub Desktop을 처음 켜면 이 순서로 안내합니다","그림 4-2")
W3=280
for i,(t) in enumerate(["첫 화면","웹 브라우저","Configure Git"]):
    x=40+i*300; y=84
    if i==1: browser(x,y,W3,360,"github.com/login/oauth…")
    else: appwin(x,y,W3,360)
    if i<2: s.p(f"M{x+W3+4},{y+180} L{x+W3+16},{y+180}")
x,y=40,84
s.t(x+20,y+44,"Welcome to",15,G,700); s.t(x+20,y+66,"GitHub Desktop",15,G,700)
for k in range(3): s.o.append(f'<line x1="{x+20}" y1="{y+96+k*16}" x2="{x+W3-30-k*30}" y2="{y+96+k*16}" stroke="{LINE}" stroke-width="5" stroke-linecap="round"/>')
button(x+20,y+160,W3-40,"Sign in to GitHub.com")
button(x+20,y+204,W3-40,"Sign in to GitHub Enterprise",primary=False)
s.t(x+20,y+264,"Skip this step",12.5,BLUE)
callout(1,x+W3-20,y+177)
x=340
s.t(x+20,y+84,"Authorize GitHub Desktop",14.5,G,700)
for k in range(3): s.o.append(f'<line x1="{x+20}" y1="{y+112+k*16}" x2="{x+W3-30-k*25}" y2="{y+112+k*16}" stroke="{LINE}" stroke-width="5" stroke-linecap="round"/>')
button(x+20,y+176,W3-40,"Authorize desktop",fill="#1F883D")
s.r(x+20,y+234,W3-40,96,"#fff",G,rx=6); s.t(x+34,y+258,"GitHub Desktop을 여시겠습니까?",12.5,G,700)
button(x+W3-150,y+286,56,"열기",h=28); button(x+W3-88,y+286,56,"취소",primary=False,h=28)
callout(2,x+W3-20,y+193); callout(3,x+W3-30,y+300)
x=640
s.t(x+20,y+36,"Configure Git",15.5,G,700)
radio(x+20,y+66,"Use my GitHub account",True); s.t(x+46,y+100,"name and email address",13.5,G)
radio(x+20,y+120,"Configure manually",False)
s.r(x+20,y+156,W3-40,88,"#F5F6F8",LINE,rx=6,sw=1); s.t(x+32,y+178,"Example commit",12,MUTE,700); s.t(x+32,y+204,"gildong-hong",13,G,700); s.t(x+32,y+226,"committed 1 minute ago",11.5,MUTE)
button(x+W3-116,y+300,96,"Finish")
callout(4,x+W3-20,y+83); callout(5,x+W3-20,y+317)
lg=[("Sign in to GitHub.com","창이 하나 더 뜨면 Continue With Browser"),("브라우저에서 로그인 후 Authorize","2단계 인증 숫자도 여기서 입력"),("GitHub Desktop 열기 허용","앱으로 돌아옵니다"),("계정의 이름과 이메일 사용","첫 번째 선택지 그대로"),("Finish","Let's get started 화면이 보이면 4장 완료")]
for i,(a,b_) in enumerate(lg):
    cx=40+(i%3)*300; cy=474+(i//3)*62
    s.b(cx+12,cy,i+1,RED); s.t(cx+34,cy+5,a,13.5,G,700); s.t(cx+34,cy+27,b_,12,MUTE)
s.save("4-02")

# ============ 5장: 첫 저장소 ============
s=S(960,550,"시작 화면에서 새 저장소 만들기를 고릅니다","그림 5-1")
appwin(40,84,540,380)
s.t(64,130,"Let's get started!",20,G,700)
s.t(64,158,"Add a repository to GitHub Desktop to start collaborating",12.5,MUTE)
opts=["Create a Tutorial Repository…","Clone a Repository from the Internet…","Create a New Repository on your Hard Drive…","Add an Existing Repository from your Hard Drive…"]
for i,t in enumerate(opts):
    y=190+i*62
    s.r(64,y,492,46,"#DCE3EC" if i==2 else "#fff",INK if i==2 else LINE,rx=6,sw=2 if i==2 else 1.5); s.t(84,y+29,t,13.5,G,700 if i==2 else 400)
callout(1,556,213+124)
legend([("Create a New Repository…","세 번째 항목. 내 PC에 새 저장소를 만듭니다"),("이 화면이 보이지 않으면","메뉴 File → New Repository…\n(두 OS 같음)")],x=620,y0=150,gap=120)
s.r(600,352,320,60,TINT,LINE,rx=6,sw=1); s.t(616,376,"Tutorial Repository는 GitHub가 준비한",12.5,MUTE); s.t(616,396,"연습 과정입니다. 이 튜토리얼에서는 쓰지 않습니다.",12.5,MUTE)
note(500)
s.save("5-01")

s=S(960,600,"새 저장소 만들기 창에서 채울 곳은 네 군데입니다","그림 5-2")
X,Y,W,H=40,84,520,440
appwin(X,Y,W,H,"Create a new repository")
field(X+20,Y+82,480,"Name","my-first-repo")
field(X+20,Y+142,480,"Description","")
field(X+20,Y+202,386,"Local path","C:\\GitHub","Choose…")
check(X+20,Y+262,"Initialize this repository with a README",True)
field(X+20,Y+306,230,"Git ignore","None"); field(X+270,Y+306,230,"License","None")
s.o.append(f'<line x1="{X}" y1="{Y+382}" x2="{X+W}" y2="{Y+382}" stroke="{LINE}"/>')
button(X+W-176,Y+396,156,"Create repository"); button(X+W-262,Y+396,76,"Cancel",primary=False)
for n,(cx,cy) in enumerate([(X+500,Y+106),(X+500,Y+226),(X+500,Y+271),(X+W-20,Y+413)],1): callout(n,cx,cy)
legend([("Name: my-first-repo","폴더 이름이자 GitHub 저장소 이름"),("Choose… 로 작업 폴더 고르기","처음이면 이 창에서 GitHub 폴더를 만듭니다\n(그림 5-3)"),("README 체크","README.md 파일과 첫 기록이 함께 생깁니다"),("Create repository","나머지 칸은 그대로 둡니다")],y0=118,gap=96)
note(560,"Local path의 예시는 Windows입니다. Mac에서는 /Users/내이름/GitHub 처럼 보입니다.")
s.save("5-02")

s=S(960,540,"Windows: 폴더 선택 창에서 GitHub 폴더를 만들고 고릅니다","그림 5-3")
X,Y,W,H=40,84,560,380
s.r(X,Y,W,H,"#fff",G,rx=6); s.r(X,Y,W,32,"#E9EDF2",G,rx=6); s.o.append(f'<rect x="{X+1}" y="{Y+20}" width="{W-2}" height="12" fill="#E9EDF2"/>'); s.t(X+14,Y+22,"폴더 선택",12.5,G,700)
s.r(X+14,Y+44,110,28,"#fff",LINE,rx=4,sw=1.5); s.t(X+69,Y+63,"새 폴더",12.5,G,700,"middle")
s.r(X+136,Y+44,W-150,28,"#fff",LINE,rx=4,sw=1); s.t(X+148,Y+63,"내 PC  >  로컬 디스크 (C:)",12.5,G)
s.o.append(f'<rect x="{X+1}" y="{Y+84}" width="150" height="{H-150}" fill="#F5F6F8"/><line x1="{X+151}" y1="{Y+84}" x2="{X+151}" y2="{Y+H-66}" stroke="{LINE}"/>')
for i,(t,hl) in enumerate([("바탕 화면",0),("문서",0),("내 PC",0),("로컬 디스크 (C:)",1)]):
    yy=Y+100+i*32
    if hl: s.r(X+6,yy-4,140,26,"#DCE3EC","#DCE3EC",rx=4)
    s.t(X+18,yy+14,t,12.5,G,700 if hl else 400)
for i,(t,hl) in enumerate([("GitHub",1),("Program Files",0),("Users",0),("Windows",0)]):
    yy=Y+100+i*32
    if hl: s.r(X+160,yy-4,W-170,26,"#DCE3EC",INK,rx=4,sw=1.5)
    s.o.append(f'<path d="M{X+172},{yy+2} h10 l3,3 h11 v12 h-24 z" fill="#E8B44A"/>'); s.t(X+204,yy+14,t,12.5,G,700 if hl else 400)
s.o.append(f'<line x1="{X}" y1="{Y+H-66}" x2="{X+W}" y2="{Y+H-66}" stroke="{LINE}"/>')
s.t(X+14,Y+H-38,"폴더:",12.5,G); field(X+56,Y+H-62,220,"","GitHub")
button(X+W-196,Y+H-50,96,"폴더 선택",h=32); button(X+W-92,Y+H-50,78,"취소",primary=False,h=32)
callout(1,X+146,Y+196); callout(2,X+124,Y+58); callout(3,X+W-18,Y+116); callout(4,X+W-100,Y+H-34)
legend([("로컬 디스크 (C:) 고르기","왼쪽 목록"),("새 폴더 → 이름 GitHub","이미 있으면 건너뜁니다"),("GitHub 폴더 한 번 클릭","들어가지 말고 선택만"),("폴더 선택","Local path가 C:\\GitHub 로 바뀝니다")],x=640,y0=118,gap=88)
note(500)
s.save("5-03-win")

s=S(960,540,"Mac: 폴더 선택 창에서 GitHub 폴더를 만들고 고릅니다","그림 5-3")
X,Y,W,H=40,84,560,380
s.r(X,Y,W,H,"#fff",G,rx=10)
s.r(X+170,Y+14,W-190,28,"#fff",LINE,rx=6,sw=1); s.t(X+184,Y+33,"hong",12.5,G,700)
s.o.append(f'<rect x="{X+1}" y="{Y+56}" width="150" height="{H-122}" fill="#F5F6F8"/><line x1="{X+151}" y1="{Y+56}" x2="{X+151}" y2="{Y+H-66}" stroke="{LINE}"/>')
s.t(X+14,Y+80,"즐겨찾기",11,MUTE,700)
for i,(t,hl) in enumerate([("응용 프로그램",0),("데스크탑",0),("문서",0),("hong (홈)",1)]):
    yy=Y+96+i*32
    if hl: s.r(X+6,yy-4,140,26,"#DCE3EC","#DCE3EC",rx=4)
    s.t(X+18,yy+14,t,12.5,G,700 if hl else 400)
for i,(t,hl) in enumerate([("GitHub",1),("Desktop",0),("Documents",0),("Downloads",0)]):
    yy=Y+80+i*32
    if hl: s.r(X+160,yy-4,W-170,26,"#DCE3EC",INK,rx=4,sw=1.5)
    s.o.append(f'<path d="M{X+172},{yy+2} h10 l3,3 h11 v12 h-24 z" fill="#5EA7F0"/>'); s.t(X+204,yy+14,t,12.5,G,700 if hl else 400)
s.o.append(f'<line x1="{X}" y1="{Y+H-66}" x2="{X+W}" y2="{Y+H-66}" stroke="{LINE}"/>')
s.r(X+14,Y+H-50,110,32,"#fff",LINE,rx=6,sw=1.5); s.t(X+69,Y+H-29,"새로운 폴더",12.5,G,700,"middle")
button(X+W-196,Y+H-50,90,"열기",h=32); button(X+W-98,Y+H-50,84,"취소",primary=False,h=32)
callout(1,X+146,Y+196); callout(2,X+124,Y+H-34); callout(3,X+W-18,Y+96); callout(4,X+W-112,Y+H-34)
legend([("홈 폴더 고르기","왼쪽 목록의 내 이름. 없으면 Shift + Cmd + H"),("새로운 폴더 → 이름 GitHub","이미 있으면 건너뜁니다"),("GitHub 폴더 한 번 클릭","들어가지 말고 선택만"),("열기 (또는 선택)","Local path가 /Users/내이름/GitHub 로 바뀝니다")],x=640,y0=118,gap=88)
note(500,"실제 화면을 단순하게 그린 그림입니다. 오른쪽 아래 버튼 이름은 버전에 따라 열기 또는 선택으로 보입니다.")
s.save("5-03-mac")

s=S(960,520,"게시(Publish) 창에서는 비공개 체크만 확인합니다","그림 5-4")
X,Y,W,H=40,84,520,360
appwin(X,Y,W,H,"Publish repository")
s.r(X+20,Y+64,120,30,"#DCE3EC",INK,rx=4,sw=1.5); s.t(X+80,Y+84,"GitHub.com",12.5,G,700,"middle")
field(X+20,Y+118,480,"Name","my-first-repo")
field(X+20,Y+178,480,"Description","")
check(X+20,Y+248,"Keep this code private",True)
s.o.append(f'<line x1="{X}" y1="{Y+300}" x2="{X+W}" y2="{Y+300}" stroke="{LINE}"/>')
button(X+W-184,Y+312,164,"Publish Repository"); button(X+W-270,Y+312,76,"Cancel",primary=False)
callout(1,X+W-30,Y+257); callout(2,X+W-20,Y+329)
legend([("Keep this code private: 체크 확인","끄면 인터넷의 누구나 볼 수 있는\n공개 저장소가 됩니다"),("Publish Repository","이름·설명은 자동으로 채워져 있습니다")],y0=160,gap=120)
note(480)
s.save("5-04")

s=S(960,580,"두 곳에 모두 있는지 확인합니다","그림 5-5")
appwin(40,84,420,330)
s.r(40,84,420,56,"#2B3138",G,rx=8); s.o.append(f'<rect x="41" y="124" width="418" height="16" fill="#2B3138"/>')
for bx,l1,l2 in ((40,"Current Repository","my-first-repo"),(250,"Fetch origin","Last fetched just now")):
    s.t(bx+18,106,l1,11,"#AEB8C4"); s.t(bx+18,126,l2,13.5,"#fff",700)
s.o.append('<line x1="250" y1="84" x2="250" y2="140" stroke="#4A525C"/>')
s.t(64,190,"No local changes",15,G,700)
for i,t in enumerate(["Open the repository in your external editor","View the files in Explorer / Finder","Open the repository page on GitHub"]):
    s.r(64,212+i*58,372,46,"#fff",LINE,rx=6,sw=1.5); s.t(80,240+i*58,t,12,G)
callout(1,436,112); callout(2,436,235); callout(3,436,351)
browser(500,84,420,330,"github.com/gildong-hong/my-first-repo")
s.t(524,168,"my-first-repo",17,G,700); s.r(650,152,64,22,"#fff",MUTE,rx=11,sw=1); s.t(682,168,"Private",11.5,MUTE,700,"middle")
s.r(524,190,372,40,"#F5F6F8",LINE,rx=6,sw=1); s.t(540,215,"README.md",12.5,G,700)
s.r(524,238,372,150,"#fff",LINE,rx=6,sw=1); s.t(544,280,"my-first-repo",22,G,700)
s.o.append('<line x1="544" y1="292" x2="876" y2="292" stroke="#C9D3DF"/>')
callout(4,722,163)
for i,(a,b_) in enumerate([("Fetch origin","Publish 버튼이 바뀌었으면 게시 완료"),("VS Code로 열기","편집기 연결 확인. 안 되면 본문 참고"),("GitHub에서 보기","브라우저에 저장소가 열립니다"),("Private 표시","비공개 저장소라는 뜻")]):
    cx=40+(i%2)*460; cy=446+(i//2)*44
    s.b(cx+12,cy,i+1,RED); s.t(cx+34,cy+5,a,13.5,G,700); s.t(cx+160,cy+5,b_,12.5,MUTE)
s.save("5-05")
