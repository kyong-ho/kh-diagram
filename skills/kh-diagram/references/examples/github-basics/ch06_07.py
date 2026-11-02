# GitHub 기초 가이드 6~7장 그림.
from course import *

# ============ 6장 ============
s=S(960,440,"저장, 커밋, 푸시는 남는 곳이 다릅니다","그림 6-1")
for x,a,b_,c,col,fl in [(40,"① 작업 폴더","지금 파일 상태","VS Code에서 저장한 그대로",INK,"#fff"),(355,"② 내 PC의 Git 기록","커밋해 둔 시점들","기록으로 남은 지점",INK,"#fff"),(670,"③ GitHub","원격 저장소","다른 사람도 볼 수 있음",GRN,GRNT)]:
    s.r(x,104,250,120,fl,col); s.t(x+18,138,a,17,col if col==GRN else G,700); s.t(x+18,168,b_,13.5,MUTE); s.t(x+18,192,c,13.5,MUTE)
s.p("M290,164 L353,164"); s.t(321,152,"커밋",14,INK,700,"middle")
s.p("M605,164 L668,164","g"); s.t(637,152,"푸시",14,GRN,700,"middle")
s.p("M795,224 L795,272 L165,272 L165,228","g",dash="5 4"); s.t(190,294,"풀: GitHub에 새로 생긴 기록을 내 PC로 받기",13.5,GRN,700)
s.o.append(f'<line x1="637" y1="176" x2="637" y2="348" stroke="{RED}" stroke-width="1.5" stroke-dasharray="3 3"/>')
s.t(622,340,"← 여기까지는 나만 봅니다",13.5,RED,700,"end"); s.t(652,340,"여기부터 남도 봅니다 →",13.5,RED,700)
s.t(40,384,"저장만 하면 ①, 커밋하면 ②까지, 푸시해야 ③까지 갑니다. 커밋하지 않은 변경은 기록에 남지 않습니다.",13.5,MUTE)
s.save("6-01")

s=S(960,640,"커밋하기 전에 Changes 화면에서 확인합니다","그림 6-2")
X,Y,W,H=40,84,880,420
lw=desktop(X,Y,W,H,action="Fetch origin",action_sub="Last fetched just now")
s.t(X+40,Y+78,"Changes 1",13.5,G,700)
check(X+16,Y+106,"README.md",True)
s.o.append(f'<line x1="{X}" y1="{Y+300}" x2="{X+lw}" y2="{Y+300}" stroke="{LINE}"/>')
field(X+16,Y+308,lw-32,"","README에 저장소 소개 추가")
s.r(X+16,Y+358,lw-32,34,BLUE,BLUE,rx=5); s.t(X+lw/2,Y+380,"Commit 1 file to main",13,"#fff",700,"middle")
s.t(X+lw+20,Y+80,"README.md",13,MUTE)
dx=X+lw+1; dw=W-lw-2
diffline(dx,Y+100,dw,"# my-first-repo"," "); diffline(dx,Y+126,dw,"(빈 줄)","+"); diffline(dx,Y+152,dw,"Git 연습용 저장소입니다.","+")
s.t(X+lw+20,Y+210,"초록색 + 는 추가된 줄, 빨간색 - 는 지워진 줄입니다",12.5,MUTE)
callout(1,X+lw-14,Y+115); callout(2,X+W-20,Y+165); callout(3,X+lw-14,Y+332); callout(4,X+lw-14,Y+375)
for i,(a,b_) in enumerate([("바뀐 파일 목록","체크된 파일만 커밋에 담깁니다"),("바뀐 내용","내가 고친 것이 맞는지 봅니다"),("한 줄 메모 (Summary)","무엇을 왜 바꿨는지"),("커밋 버튼","버튼에 적힌 브랜치 이름도 확인")]):
    cx=40+(i%2)*460; cy=530+(i//2)*44
    s.b(cx+12,cy,i+1,RED); s.t(cx+34,cy+5,a,13.5,G,700); s.t(cx+210,cy+5,b_,12.5,MUTE)
s.save("6-02")

s=S(960,500,"위쪽 오른쪽 버튼은 상황에 따라 이름이 바뀝니다","그림 6-3")
rows=[("Publish repository","GitHub에 아직 없음","5장에서 한 번 누름. 처음 올리기(게시)",None),
      ("Fetch origin","확인할 것만 있음","눌러도 내 파일은 바뀌지 않음. GitHub에 새 소식이 있는지 확인",None),
      ("Push origin","↑1","올릴 커밋이 1개 있음. 누르면 GitHub로 올라감(푸시)","g"),
      ("Pull origin","↓1","받을 커밋이 1개 있음. 누르면 내 PC로 내려옴(풀)","i")]
for i,(lab,badge,desc,c) in enumerate(rows):
    y=90+i*86
    s.r(40,y,300,62,"#2B3138","#2B3138",rx=6); s.t(60,y+26,lab,15,"#fff",700)
    s.t(60,y+48,badge,12.5,"#AEB8C4" if c is None else ("#7CCF9C" if c=="g" else "#8FB8E6"),700)
    s.t(370,y+28,desc.split(". ")[0],15,G,700)
    if ". " in desc: s.t(370,y+50,desc.split(". ",1)[1],13,MUTE)
s.t(40,448,"Push와 Pull이 둘 다 필요하면 Pull을 먼저 합니다. 작업을 시작할 때는 Fetch origin을 한 번 누르는 습관을 들입니다.",13.5,MUTE)
s.save("6-03")

s=S(960,540,"GitHub 웹사이트에서 파일 고치기 (받기 연습용)","그림 6-4")
PW=280
for i,(url,t) in enumerate([("…/my-first-repo/blob/main/README.md","파일 화면"),("…/my-first-repo/edit/main/README.md","고치는 화면"),("…/my-first-repo/edit/main/README.md","기록 남기기")]):
    x=40+i*300; browser(x,84,PW,340,url)
    if i<2: s.p(f"M{x+PW+4},254 L{x+PW+16},254")
x=40
s.t(x+20,150,"README.md",14,G,700)
s.r(x+PW-54,136,34,28,"#fff",LINE,rx=5); s.o.append(f'<path d="M{x+PW-45},{157} l3,-9 l12,-12 l6,6 l-12,12 z" fill="none" stroke="{G}" stroke-width="2" stroke-linejoin="round"/>')
s.r(x+20,178,PW-40,120,"#fff",LINE,rx=6,sw=1); s.t(x+36,212,"my-first-repo",18,G,700); s.t(x+36,244,"Git 연습용 저장소입니다.",12.5,G)
callout(1,x+PW-18,150)
x=340
s.r(x+20,136,PW-40,190,"#fff",LINE,rx=6,sw=1)
for k,(t,c) in enumerate([("# my-first-repo",G),("",G),("Git 연습용 저장소입니다.",G),("웹에서 추가한 줄",GRN)]):
    s.t(x+32,164+k*24,t,12.5,c,700 if c==GRN else 400)
s.r(x+PW-164,340,130,32,"#1F883D","#1F883D",rx=5); s.t(x+PW-99,361,"Commit changes…",12.5,"#fff",700,"middle")
callout(2,x+PW-18,356)
x=640
s.r(x+20,120,PW-40,260,"#fff",G,rx=8); s.t(x+36,148,"Commit changes",14,G,700)
field(x+36,168,PW-72,"Commit message","웹에서 한 줄 추가")
s.r(x+PW-150,330,110,32,"#1F883D","#1F883D",rx=5); s.t(x+PW-95,351,"Commit changes",12,"#fff",700,"middle")
callout(3,x+PW-24,346)
for i,(a,b_) in enumerate([("연필 아이콘","파일 고치기(Edit this file)"),("Commit changes…","고친 뒤 누릅니다"),("메모 쓰고 Commit changes","GitHub에 바로 기록됩니다")]):
    cx=40+i*300; cy=456
    s.b(cx+12,cy,i+1,RED); s.t(cx+34,cy+5,a,13.5,G,700); s.t(cx+34,cy+27,b_,12,MUTE)
s.save("6-04")

# ============ 7장 ============
s=S(960,500,"되돌리기는 커밋·푸시 여부에 따라 방법이 다릅니다","그림 7-1")
s.r(60,84,240,56,TINT,INK,rx=28); s.t(180,118,"이미 커밋했나요?",15.5,INK,700,"middle")
s.r(500,84,260,56,TINT,INK,rx=28); s.t(630,118,"GitHub에 올렸나요(푸시)?",15.5,INK,700,"middle")
s.p("M300,112 L496,112"); s.t(398,102,"예",13.5,INK,700,"middle")
s.p("M180,140 L180,236"); s.t(192,194,"아니요",13.5,INK,700)
s.p("M590,140 L490,236"); s.t(520,194,"아니요",13.5,INK,700,"end")
s.p("M670,140 L770,236"); s.t(740,194,"예",13.5,INK,700)
boxes=[(40,INK,"Discard Changes","커밋 전 변경 버리기",["· 고른 파일만, 마지막 커밋 상태로","· 기록에 남지 않음"],"· 필요한 수정도 같이 사라짐"),
       (340,INK,"Undo","방금 한 커밋 취소",["· 가장 최근 커밋 하나만","· 변경은 Changes로 돌아옴"],"· 푸시하기 전에만 보임"),
       (640,GRN,"Revert Changes in Commit","변경을 취소하는 새 커밋",["· 고른 커밋 하나의 변경만","· 실수한 커밋도 기록에 남음"],"· 폴더 전체를 되감는 것이 아님")]
for x,col,t1,t2,ls,warn in boxes:
    s.r(x,240,280,160,"#fff",col); s.t(x+18,272,t1,16.5,col,700); s.t(x+18,298,t2,13.5,G,700)
    for k,l in enumerate(ls): s.t(x+18,328+k*22,l,12.5,MUTE)
    s.t(x+18,372,warn,12.5,RED,700)
s.t(40,440,"여러 커밋을 한꺼번에 되감고 싶거나, 되돌리다 충돌(10장) 안내가 뜨면 직접 해결하지 말고 멈춘 뒤 도움을 요청합니다.",13.5,MUTE)
s.save("7-01")

s=S(960,520,"푸시 전: 방금 한 커밋은 Undo로 취소합니다","그림 7-5")
X,Y=40,84
desktop(X,Y,520,340,branch="main",action="Push origin",action_sub="↑ 1")
s.t(X+125,Y+200,"No local changes",12.5,MUTE,400,"middle")
s.o.append(f'<line x1="{X}" y1="{Y+258}" x2="{X+250}" y2="{Y+258}" stroke="{LINE}"/>')
s.t(X+14,Y+282,"Committed just now",11,MUTE); s.t(X+14,Y+304,"되돌리기 연습용 메모",12.5,G,700)
s.r(X+176,Y+284,62,28,"#fff",LINE,rx=4,sw=1.5); s.t(X+207,Y+303,"Undo",12.5,G,700,"middle")
callout(1,X+244,Y+284); callout(2,X+500,Y+2)
for i,(a,b_) in enumerate([("Undo 누르기","Changes 아래쪽, 커밋 직후에 보입니다"),("Push origin 전이어야 합니다","↑1은 아직 올리지 않은 커밋이 1개라는 뜻"),("결과","변경은 Changes로, 메모는 Summary 칸으로 돌아옵니다.\n고쳐서 다시 커밋합니다")]):
    y=118+i*96; s.b(610,y,i+1,RED if i<2 else INK); s.t(636,y+6,a,15,G,700)
    for k,l in enumerate(b_.split("\n")): s.t(636,y+30+k*19,l,12.5,MUTE)
s.t(40,470,"이미 푸시한 커밋은 Undo가 나타나지 않습니다. 그때는 Revert Changes in Commit을 씁니다.",13.5,MUTE)
s.save("7-05")

s=S(960,570,"커밋 전: 파일을 오른쪽 클릭해 Discard Changes","그림 7-2")
X,Y=40,84
lw=desktop(X,Y,420,380,action="Fetch origin",action_sub="Fetched")
s.t(X+40,Y+78,"Changes 1",13.5,G,700)
s.r(X+6,Y+100,lw-12,28,"#DCE3EC","#DCE3EC",rx=4); check(X+16,Y+105,"README.md",True)
s.r(X+120,Y+124,230,190,"#fff",G,rx=6)
for i,t in enumerate(["Discard Changes…","Ignore File (Add to .gitignore)","Copy File Path","Show in Explorer / Finder","Open in Visual Studio Code"]):
    yy=Y+132+i*34
    if i==0: s.r(X+124,yy,222,28,"#DCE3EC","#DCE3EC",rx=4)
    s.t(X+136,yy+19,t,12.5,G,700 if i==0 else 400)
callout(1,X+346,Y+146)
appwin(500,84,420,300,"Confirm Discard Changes")
s.t(520,170,"Are you sure you want to discard",13,G); s.t(520,190,"all changes to:",13,G)
s.r(520,206,380,40,"#F5F6F8",LINE,rx=4,sw=1); s.t(536,232,"README.md",13.5,G,700)
s.o.append('<line x1="500" y1="320" x2="920" y2="320" stroke="#C9D3DF"/>')
button(500+420-176,332,156,"Discard Changes",fill="#C2362B"); button(500+420-262,332,76,"Cancel",primary=False)
callout(2,900,226); callout(3,900,349)
for i,(a,b_) in enumerate([("Discard Changes…","버릴 파일에서 오른쪽 클릭"),("파일 이름 확인","이 파일의 커밋 안 한 변경이 모두 사라집니다"),("Discard Changes","확인 후 누름. 헷갈리면 Cancel")]):
    cx=40+i*300; cy=486
    s.b(cx+12,cy,i+1,RED); s.t(cx+34,cy+5,a,13.5,G,700); s.t(cx+34,cy+27,b_,12,MUTE)
s.save("7-02")

s=S(960,590,"커밋 후: History에서 커밋을 오른쪽 클릭해 Revert","그림 7-3")
X,Y=40,84
lw=desktop(X,Y,540,380,action="Fetch origin",action_sub="Last fetched just now",tab="History")
for i,(t,sub) in enumerate([("되돌리기 연습용 실수","방금"),("회의록 양식 추가","10분 전"),("README에 저장소 소개 추가","20분 전"),("Initial commit","어제")]):
    yy=Y+100+i*52
    if i==0: s.r(X+6,yy-4,lw-12,46,"#DCE3EC","#DCE3EC",rx=4)
    s.t(X+18,yy+16,t if len(t)<14 else t[:12]+"…",13,G,700 if i==0 else 400); s.t(X+18,yy+34,sub,11,MUTE)
s.r(X+170,Y+120,300,212,"#fff",G,rx=6)
for i,t in enumerate(["Reset to Commit…","Checkout Commit","Revert Changes in Commit","Create Branch from Commit","Create Tag…","Copy SHA"]):
    yy=Y+128+i*33
    if i==2: s.r(X+174,yy,292,28,"#DCE3EC","#DCE3EC",rx=4)
    s.t(X+186,yy+19,t,12.5,G,700 if i==2 else MUTE if i<2 else 400)
callout(1,X+lw-14,Y+118); callout(2,X+468,Y+209)
s.r(620,120,300,190,GRNT,GRN,rx=8); s.t(640,150,"결과: 맨 위에 새 커밋",14.5,GRN,700)
s.r(636,168,268,46,"#fff",LINE,rx=4,sw=1); s.t(648,188,'Revert "되돌리기 연습용 실수"',12.5,G,700); s.t(648,206,"방금",11,MUTE)
s.r(636,220,268,40,"#fff",LINE,rx=4,sw=1); s.t(648,244,"되돌리기 연습용 실수",12.5,MUTE)
s.t(640,286,"그다음 Push origin 으로 올립니다",12.5,G,700)
callout(3,904,191)
for i,(a,b_) in enumerate([("History 탭에서 커밋 고르기","되돌릴 커밋을 오른쪽 클릭"),("Revert Changes in Commit","위의 Reset, Checkout은 누르지 않음"),("취소 커밋 확인 후 푸시","실수한 커밋은 그대로 남음")]):
    cx=40+i*300; cy=504
    s.b(cx+12,cy,i+1,RED); s.t(cx+34,cy+5,a,13.5,G,700); s.t(cx+34,cy+27,b_,12,MUTE)
s.save("7-03")

s=S(960,420,"Revert는 취소 커밋을 하나 더 만드는 것입니다","그림 7-4")
s.o.append(f'<line x1="60" y1="190" x2="900" y2="190" stroke="{INK}" stroke-width="3"/>')
cs=[("1","Initial commit",INK),("2","README에 저장소 소개",INK),("3","회의록 양식 추가",INK),("4","되돌리기 연습용 실수",RED),("5 (Revert)","4번의 변경을 취소",GRN)]
for i,(d,m,c) in enumerate(cs):
    x=120+i*180
    s.o.append(f'<circle cx="{x}" cy="190" r="13" fill="#fff" stroke="{c}" stroke-width="4"/>')
    s.o.append(f'<line x1="{x}" y1="203" x2="{x}" y2="232" stroke="{c}" stroke-width="1.5"/>')
    s.r(x-84,232,168,70,REDT if c==RED else (GRNT if c==GRN else "#fff"),c)
    s.t(x,254,d+"번 커밋" if "Revert" not in d else "5번 커밋 (Revert)",12.5,MUTE,400,"middle")
    words=m.split(" "); l1=" ".join(words[:2]); l2=" ".join(words[2:])
    s.t(x,274,l1,13.5,c if c!=INK else G,700,"middle")
    if l2: s.t(x,292,l2,13.5,c if c!=INK else G,700,"middle")
s.p("M832,170 C 812,100 688,100 668,168","r",dash="6 4"); s.t(750,96,"이 커밋이 만든 변경만 취소",14,RED,700,"middle")
s.t(40,338,"4번 커밋은 기록에 그대로 남습니다. 폴더 전체가 3번 시점으로 되감기는 것이 아니라,",13.5,MUTE)
s.t(40,360,"4번이 바꾼 부분만 원래대로 돌려놓는 새 커밋이 생깁니다. 그 뒤에 한 수정은 그대로 남습니다.",13.5,MUTE)
s.save("7-04")
