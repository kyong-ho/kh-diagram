# GitHub 기초 가이드 8~13장 그림.
from course import *

# ============ 8장 ============
s=S(960,470,"브랜치: 한 시점에서 갈라져 나와 따로 자라는 줄","그림 8-1")
MY,WY=150,320
s.o.append(f'<line x1="150" y1="{MY}" x2="910" y2="{MY}" stroke="{GRN}" stroke-width="4" stroke-linecap="round"/>')
s.o.append(f'<path d="M330,{MY} C 372,{MY} 360,{WY} 412,{WY} L 910,{WY}" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
lane(MY,GRN,"main"); lane(WY,INK,"work")
for x in (190,260,330): dot(x,MY,GRN)
s.t(330,MY-26,"분기점",14,G,700,"middle"); s.t(330,MY-46,"여기서 갈라져 나옴",12.5,MUTE,400,"middle")
for x in (520,640,760): dot(x,WY,INK)
s.t(640,WY+36,"work에 쌓은 커밋",13.5,INK,700,"middle")
s.o.append(f'<line x1="640" y1="{MY+16}" x2="640" y2="{WY-16}" stroke="{MUTE}" stroke-width="2" stroke-dasharray="5 5"/>')
s.o.append(f'<circle cx="640" cy="235" r="15" fill="#fff" stroke="{RED}" stroke-width="2.5"/><path d="M633,228 L647,242 M647,228 L633,242" stroke="{RED}" stroke-width="3" stroke-linecap="round"/>')
s.t(662,231,"main에는",13.5,RED,700); s.t(662,250,"자동으로 들어가지 않음",13.5,RED,700)
s.t(40,410,"갈라지기 전까지의 기록은 둘이 같고, 갈라진 뒤에는 따로 자랍니다. 한쪽의 커밋을 다른 쪽에 넣으려면",13.5,MUTE)
s.t(40,432,"병합(merge)이라는 별도 단계가 필요합니다(9장).",13.5,MUTE)
s.save("8-01")

s=S(960,620,"Current Branch에서 새 브랜치를 만듭니다","그림 8-2")
X,Y=40,84
desktop(X,Y,420,380,branch="main",action="Fetch origin",action_sub="Last fetched")
s.r(X+140,Y+52,280,200,"#fff",G,rx=6)
s.r(X+150,Y+62,160,28,"#fff",LINE,rx=4,sw=1); s.t(X+160,Y+81,"Filter",12,"#9AA5B1")
s.r(X+318,Y+62,92,28,BLUE,BLUE,rx=4); s.t(X+364,Y+81,"New Branch",12,"#fff",700,"middle")
s.t(X+152,Y+116,"Default branch",11,MUTE,700); s.r(X+146,Y+124,268,28,"#DCE3EC","#DCE3EC",rx=4); s.t(X+160,Y+143,"✓  main",12.5,G,700)
callout(1,X+262,Y+2); callout(2,X+426,Y+76)
appwin(500,84,420,380,"Create a Branch")
field(520,160,380,"Name","work")
s.t(520,236,"Create branch based on…",13,G,700)
radio(520,252,"main",True); radio(520,280,"",False); s.t(546,294,"(다른 브랜치가 있으면 여기에 나옴)",12,MUTE)
s.o.append('<line x1="500" y1="400" x2="920" y2="400" stroke="#C9D3DF"/>')
button(920-156,414,136,"Create Branch"); button(920-240,414,76,"Cancel",primary=False)
callout(3,900,184); callout(4,506,261); callout(5,918,416)
legend_row([("Current Branch 누르기","지금 브랜치 이름이 보이는 곳"),("New Branch","목록 위쪽 파란 버튼"),("Name: work","이 튜토리얼에서 쓰는 이름"),("main 기준","main에서 갈라져 나옵니다"),("Create Branch","이제 Current Branch가 work")],486,cols=3)
s.save("8-02")

s=S(960,500,"브랜치를 바꾸면 폴더 안의 파일도 바뀝니다","그림 8-3")
for i,(br,col,lines) in enumerate((("work",INK,["# my-first-repo","","Git 연습용 저장소입니다.","웹에서 추가한 줄","작업 브랜치에서 추가한 줄"]),("main",GRN,["# my-first-repo","","Git 연습용 저장소입니다.","웹에서 추가한 줄",""]))):
    x=40+i*460
    s.r(x,90,420,52,"#2B3138","#2B3138",rx=6); s.t(x+18,112,"Current Branch",10.5,"#AEB8C4"); s.t(x+18,132,br,14,"#fff",700)
    s.r(x,152,420,220,"#fff",col,rx=6,sw=2); s.t(x+18,178,"VS Code  ·  README.md",12.5,MUTE,700)
    for k,l in enumerate(lines):
        if l=="작업 브랜치에서 추가한 줄": s.r(x+10,190+k*30,400,26,GRNT,GRNT,rx=3)
        s.t(x+22,208+k*30,l,13,GRN if l=="작업 브랜치에서 추가한 줄" else G,700 if l=="작업 브랜치에서 추가한 줄" else 400)
    if i==1: s.r(x+10,190+4*30,400,26,"none",RED,rx=3,dash="5 4"); s.t(x+22,208+4*30,"(없음)",13,RED,700)
s.p("M462,262 L496,262"); s.t(479,250,"전환",12.5,INK,700,"middle")
s.t(40,418,"같은 폴더(my-first-repo)인데, Current Branch를 main으로 바꾸면 work에서 한 커밋의 내용이 사라진 것처럼 보입니다.",13.5,MUTE)
s.t(40,440,"지워진 것이 아닙니다. work로 다시 바꾸면 돌아옵니다. Git이 폴더 내용을 그 브랜치의 기록에 맞춰 바꿔 보여 줍니다.",13.5,MUTE)
s.save("8-03")

s=S(960,470,"커밋하지 않은 변경이 있을 때 브랜치를 바꾸면","그림 8-4")
appwin(40,84,480,300,"Switch Branch")
s.t(60,164,"You have changes on this branch.",13,G); s.t(60,184,"What would you like to do with them?",13,G)
radio(60,210,"Leave my changes on work",True); s.t(86,244,"",12,MUTE)
radio(60,256,"Bring my changes to main",False)
s.o.append('<line x1="40" y1="320" x2="520" y2="320" stroke="#C9D3DF"/>')
button(520-156,334,136,"Switch Branch"); button(520-240,334,76,"Cancel",primary=False)
callout(1,520-252,351)
s.r(560,110,360,230,TINT,INK,rx=8)
s.t(580,142,"이 튜토리얼의 규칙",15,INK,700)
s.t(580,176,"① 이 창이 뜨면 Cancel",14,G,700)
s.t(580,204,"② 지금 브랜치에서 먼저 커밋",14,G,700)
s.t(580,232,"③ 그다음 브랜치를 바꿈",14,G,700)
s.t(580,272,"두 선택지는 변경을 잠시 보관하거나(stash)",12.5,MUTE); s.t(580,292,"다른 브랜치로 옮기는 기능입니다.",12.5,MUTE); s.t(580,312,"처음에는 쓰지 않습니다.",12.5,MUTE)
s.t(40,420,"브랜치를 바꾸기 전에 Changes가 비어 있는지 보는 습관을 들이면 이 창을 만날 일이 없습니다.",13.5,MUTE)
s.save("8-04")

# ============ 9장 ============
s=S(960,440,"PR은 요청이고, 병합은 실제로 합치는 것입니다","그림 9-1")
steps=[("① PR 만들기","work → main","“합쳐 주세요” 요청",INK,"#fff"),("② 검토","바뀐 내용 확인","의견·수정 요청",INK,"#fff"),("③ 병합 (merge)","Merge pull request","이때 main이 바뀜",GRN,GRNT)]
for i,(a,b_,c,col,fl) in enumerate(steps):
    x=40+i*300
    s.r(x,100,270,150,fl,col); s.t(x+22,136,a,17,col if col==GRN else G,700); s.t(x+22,172,b_,13.5,G); s.t(x+22,204,c,13.5,MUTE)
    if i<2: s.p(f"M{x+272},175 L{x+298},175")
s.p("M475,250 C 475,312 330,312 330,254","r",dash="6 4"); s.t(402,330,"수정 요청이 오면 work에서 고쳐 다시 푸시 → 같은 PR에 반영",13,RED,700,"middle")
s.t(40,386,"PR을 만들어도 main은 그대로입니다. ③ 병합을 눌러야 main에 들어갑니다. 혼자 쓰는 저장소에서는 ②를 스스로 확인합니다.",13.5,MUTE)
s.save("9-01")

s=S(960,620,"work를 올리고 PR 만들기 화면으로 갑니다","그림 9-2")
X,Y=40,84
desktop(X,Y,420,360,branch="work",action="Publish branch",action_sub="to GitHub")
s.t(X+270,Y+170,"No local changes",14,G,700,"middle")
s.r(X+30,Y+200,370,60,"#fff",LINE,rx=6,sw=1.5); s.t(X+44,Y+224,"Create a Pull Request from your",12,G); s.t(X+44,Y+242,"current branch",12,G)
s.r(X+250,Y+215,140,32,BLUE,BLUE,rx=4); s.t(X+320,Y+236,"Preview Pull Request",11,"#fff",700,"middle")
callout(1,X+400,Y+2); callout(2,X+400,Y+231)
appwin(500,84,420,360,"Open a Pull Request")
s.r(520,152,120,28,"#DCE3EC",INK,rx=4,sw=1.5); s.t(532,171,"base: main",12.5,G,700); caret(620,164,G)
s.t(652,171,"←  work",12.5,G,700)
s.t(520,210,"Changes 1 file · 1 commit",12.5,MUTE)
diffline(501,224,418,"작업 브랜치에서 추가한 줄","+")
s.r(520,270,380,34,GRNT,GRN,rx=4,sw=1); s.t(534,292,"✓ Able to merge.",12.5,GRN,700)
s.o.append('<line x1="500" y1="380" x2="920" y2="380" stroke="#C9D3DF"/>')
button(920-176,392,156,"Create Pull Request")
callout(3,506,166); callout(4,918,394)
legend_row([("Publish branch","work를 GitHub에 처음 올림"),("Preview Pull Request","가운데의 파란 버튼"),("base: main 확인","main 쪽으로 합쳐 달라는 뜻"),("Create Pull Request","브라우저에서 PR 작성 화면이 열림")],486,cols=2,w=460)
s.save("9-02")

s=S(960,680,"GitHub에서 PR을 만들고 병합합니다","그림 9-3")
browser(40,84,420,440,"github.com/…/my-first-repo/compare/main...work")
s.t(60,160,"Open a pull request",16,G,700)
s.r(60,176,380,28,"#F5F6F8",LINE,rx=4,sw=1); s.t(72,195,"base: main  ←  compare: work",12.5,G,700)
field(60,222,380,"Add a title","작업 브랜치에서 한 줄 추가")
s.t(60,300,"Add a description",13,G,700); s.r(60,308,380,90,"#fff",LINE,rx=4,sw=1.5); s.t(72,332,"README에 한 줄을 추가했습니다.",12.5,G)
button(260,420,180,"Create pull request",fill="#1F883D")
callout(1,440,190); callout(2,440,420+17)
browser(500,84,420,440,"github.com/…/my-first-repo/pull/1")
s.t(520,160,"작업 브랜치에서 한 줄 추가 #1",15,G,700)
s.r(520,172,56,22,"#1F883D","#1F883D",rx=11); s.t(548,188,"Open",11.5,"#fff",700,"middle")
for i,t in enumerate(["Conversation","Commits 1","Files changed 1"]):
    s.t(530+i*120,224,t,12.5,G if i==0 else MUTE,700 if i==0 else 400)
s.o.append('<line x1="500" y1="234" x2="920" y2="234" stroke="#C9D3DF"/>')
s.r(520,300,380,150,"#fff",LINE,rx=6,sw=1.5); s.t(536,326,"This branch has no conflicts with the base branch",12,GRN,700)
s.r(536,344,190,32,"#1F883D","#1F883D",rx=5); s.t(622,365,"Merge pull request",12.5,"#fff",700,"middle"); caret(700,358,"#fff")
s.r(536,382,260,58,"#fff",G,rx=4,sw=1); s.r(540,386,252,24,"#DCE3EC","#DCE3EC",rx=3); s.t(550,403,"✓ Create a merge commit",11.5,G,700); s.t(550,428,"Squash and merge · Rebase and merge",11,MUTE)
callout(3,898,219); callout(4,810,398)
s.t(520,480,"→ Confirm merge 를 누르면 병합 완료",12.5,INK,700)
legend_row([("base: main ← compare: work","방향 확인"),("Create pull request","제목·설명을 쓰고 누름"),("Files changed 탭","바뀐 내용을 한 번 더 확인"),("Create a merge commit 선택","Merge pull request → Confirm merge")],548-6,cols=2,w=460)
s.save("9-03")

s=S(960,520,"병합한 뒤: 브랜치는 지우지 않고, 내 PC의 main도 받습니다","그림 9-4")
browser(40,84,420,300,"github.com/…/my-first-repo/pull/1")
s.r(60,156,56,22,"#8250DF","#8250DF",rx=11); s.t(88,172,"Merged",11.5,"#fff",700,"middle")
s.r(60,196,380,120,"#fff",LINE,rx=6,sw=1.5); s.t(76,226,"Pull request successfully merged and closed",12,G,700)
s.t(76,248,"You're all set — the work branch can be",11.5,MUTE); s.t(76,266,"safely deleted.",11.5,MUTE)
s.r(310,276,116,28,"#fff",RED,rx=4,sw=1.5); s.t(368,295,"Delete branch",12,RED,700,"middle")
s.o.append(f'<path d="M300,272 L436,308 M436,272 L300,308" stroke="{RED}" stroke-width="2.5"/>')
callout(1,440,290)
X,Y=500,84
desktop(X,Y,420,300,branch="main",action="Pull origin",action_sub="↓ 2")
s.t(X+270,Y+170,"main으로 바꾼 뒤",13,G,700,"middle"); s.t(X+270,Y+194,"Fetch origin → Pull origin",13,G,700,"middle")
callout(2,X+262,Y+2); callout(3,X+400,Y+2)
legend_row([("Delete branch는 누르지 않음","이 튜토리얼은 work를 계속 씁니다"),("Current Branch → main","내 PC의 main은 아직 옛날 상태"),("Fetch → Pull origin","병합된 내용이 내 PC의 main에 들어옴")],430,cols=3)
s.save("9-04")

s=S(960,480,"같은 work로 계속 작업하고 두 번째 PR을 만듭니다","그림 9-5")
MY,WY=150,320
s.o.append(f'<line x1="150" y1="{MY}" x2="910" y2="{MY}" stroke="{GRN}" stroke-width="4" stroke-linecap="round"/>')
s.o.append(f'<path d="M230,{MY} C 262,{MY} 252,{WY} 292,{WY} L 910,{WY}" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
lane(MY,GRN,"main"); lane(WY,INK,"work")
dot(190,MY,GRN); dot(230,MY,GRN)
dot(360,WY,INK); s.t(360,WY+34,"첫 번째 작업",12.5,MUTE,400,"middle")
s.p(f"M368,{WY-12} L452,{MY+14}","i",dash="6 4"); dot(460,MY,GRN,True); s.t(460,MY-26,"PR #1 병합",13.5,GRN,700,"middle")
dot(620,WY,INK); s.t(620,WY+34,"두 번째 작업",12.5,MUTE,400,"middle")
s.p(f"M628,{WY-12} L752,{MY+14}","i",dash="6 4"); dot(760,MY,GRN,True); s.t(760,MY-26,"PR #2 병합",13.5,GRN,700,"middle")
s.r(560,208,170,44,"#fff",INK,rx=22,sw=2); s.t(645,236,"PR #2에는 이것만",13,INK,700,"middle")
s.t(40,394,"병합 방식을 Create a merge commit으로 하면, 두 번째 PR에는 첫 병합 뒤에 새로 한 커밋만 나타납니다.",13.5,MUTE)
s.t(40,416,"Squash and merge로 병합했다면 이미 들어간 커밋이 다시 보일 수 있습니다. 그래서 이 튜토리얼은 merge commit을 씁니다.",13.5,MUTE)
s.save("9-05")

# ============ 10장 ============
s=S(960,540,"충돌은 같은 곳을 양쪽에서 다르게 고쳤을 때만 납니다","그림 10-1")
rowsx=[(84,GRN,GRNT,"다른 곳을 고쳤을 때","README의 소개 문장을 고침","회의록 양식을 고침","서로 다른 곳이라 Git이 자동으로 합칩니다. 충돌 없음"),
       (292,RED,REDT,"같은 곳을 다르게 고쳤을 때","소개 문장 끝에 (A)를 붙임","소개 문장 끝에 (B)를 붙임","같은 줄입니다. 어느 쪽이 맞는지 Git은 판단하지 않습니다. 사람이 정해야 합니다 = 충돌")]
for y,c,ct,ttl,l,r,res in rowsx:
    s.t(40,y+18,ttl,16,c,700)
    s.r(40,y+32,410,70,"#fff",INK); s.t(58,y+60,"work에서",13,INK,700); s.t(58,y+84,l,15,G,700)
    s.r(510,y+32,410,70,"#fff",GRN); s.t(528,y+60,"main에서",13,GRN,700); s.t(528,y+84,r,15,G,700)
    s.t(480,y+74,"+",24,MUTE,700,"middle")
    s.p(f"M245,{y+102} L245,{y+124}","m",sw=1.5); s.p(f"M715,{y+102} L715,{y+124}","m",sw=1.5)
    s.r(40,y+126,880,44,ct,c); s.t(58,y+154,res,14.5,c,700)
s.t(40,498,"충돌은 고장이 아닙니다. “둘 중 어느 쪽이 맞나요?”라는 Git의 질문입니다.",13.5,MUTE)
s.save("10-01")

s=S(960,590,"병합 전에 충돌이 날지 미리 알려 줍니다","그림 10-2")
X,Y=40,84
desktop(X,Y,380,340,branch="work",action="Fetch origin",action_sub="Last fetched")
dropdown(X+110,Y+52,270,["main","work"],hl=None,header="Filter")
s.r(X+116,Y+180,250,30,"#fff",BLUE,rx=4,sw=1.5); s.t(X+241,Y+200,"Choose a branch to merge into work",11,BLUE,700,"middle")
callout(1,X+236,Y+2); callout(2,X+372,Y+195)
appwin(460,84,460,340,"Merge into work")
s.r(480,150,420,28,"#fff",LINE,rx=4,sw=1); s.t(492,169,"Filter",12,"#9AA5B1")
s.r(480,188,420,28,"#DCE3EC","#DCE3EC",rx=4); s.t(494,207,"main",12.5,G,700)
s.r(480,300,420,40,REDT,RED,rx=4,sw=1); s.t(494,318,"⚠ There will be 1 conflicted file when merging",11.5,RED,700); s.t(494,334,"main into work",11.5,RED,700)
s.o.append('<line x1="460" y1="356" x2="920" y2="356" stroke="#C9D3DF"/>')
button(920-196,370,176,"Create a merge commit")
callout(3,900,202); callout(4,900,320); callout(5,918,372)
legend_row([("Current Branch","work가 선택된 상태에서"),("Choose a branch to merge…","목록 아래쪽"),("main 고르기","main을 work로 합칩니다"),("충돌 예고","이번 실습에서는 일부러 낸 것"),("Create a merge commit","누르면 충돌 창이 뜹니다")],450,cols=3)
s.save("10-02")

s=S(960,470,"충돌 창이 뜨면 Abort merge로 빠져나옵니다","그림 10-3")
X,Y=40,84
s.r(X,Y,500,300,"#fff",G,rx=8); s.t(X+20,Y+34,"Resolve conflicts before Merge",15.5,G,700)
s.o.append(f'<line x1="{X}" y1="{Y+52}" x2="{X+500}" y2="{Y+52}" stroke="{LINE}"/>')
s.t(X+20,Y+82,"1 conflicted file",13.5,MUTE)
s.r(X+20,Y+96,460,52,"#fff",LINE,rx=4,sw=1.5); s.t(X+36,Y+120,"README.md",14,G,700); s.t(X+36,Y+138,"1 conflict",12,RED)
s.r(X+330,Y+108,138,28,"#fff",LINE,rx=4,sw=1.5); s.t(X+390,Y+127,"Open in editor",12.5,MUTE,400,"middle"); caret(X+446,Y+120,MUTE)
s.o.append(f'<line x1="{X}" y1="{Y+236}" x2="{X+500}" y2="{Y+236}" stroke="{LINE}"/>')
s.r(X+210,Y+252,130,34,"#fff",RED,rx=5,sw=2.5); s.t(X+275,Y+274,"Abort merge",13.5,RED,700,"middle")
s.r(X+352,Y+252,130,34,"#E8ECF1",LINE,rx=5); s.t(X+417,Y+274,"Continue merge",13.5,"#9AA5B1",700,"middle")
callout(1,X+210,Y+252)
for i,(a,b_) in enumerate([("멈춥니다","다른 버튼을 누르지 않습니다"),("Abort merge","병합을 시작하기 직전으로 돌아갑니다"),("확인","Changes가 비어 있고, work의 커밋은 그대로")]):
    y=108+i*80; s.b(600,y,i+1,RED if i==1 else INK); s.t(624,y+5,a,16,G,700); s.t(624,y+28,b_,13,MUTE)
s.t(40,420,"Continue merge는 모든 충돌을 해결한 뒤에만 눌리는 버튼입니다. 해결 방법은 10장 끝의 심화에 있습니다.",13.5,MUTE)
s.save("10-03")

s=S(960,540,"심화: VS Code에서 충돌 표시를 정리하는 모습","그림 10-4")
s.r(40,84,880,300,"#1E1E1E","#1E1E1E",rx=8)
s.t(60,112,"README.md",12.5,"#CCCCCC",700)
acc=[(76,"Accept Current Change"),(246,"Accept Incoming Change"),(424,"Accept Both Changes"),(578,"Compare Changes")]
for k,(ax,at) in enumerate(acc):
    s.t(ax,156,at,12,"#9CDCFE")
    if k: s.t(ax-10,156,"|",12,"#6A6A6A")
rows=[("<<<<<<< HEAD (Current Change)","#3A5F4B","#9CDCFE"),("Git 연습용 저장소입니다. (A)","#29473A","#D4D4D4"),("=======","#1E1E1E","#9CDCFE"),("Git 연습용 저장소입니다. (B)","#2A3C5A","#D4D4D4"),(">>>>>>> main (Incoming Change)","#344B6E","#9CDCFE")]
for i,(t,bg,fg) in enumerate(rows):
    y=170+i*30; s.o.append(f'<rect x="60" y="{y}" width="840" height="28" fill="{bg}"/>'); s.t(76,y+19,t,13,fg)
callout(1,146,132); callout(2,322,132); callout(3,488,132)
s.t(60,360,"위쪽이 지금 브랜치(work, Current), 아래쪽이 합치려는 브랜치(main, Incoming)의 내용입니다.",12.5,"#CCCCCC")
legend_row([("Accept Current Change","work 쪽만 남김"),("Accept Incoming Change","main 쪽만 남김"),("Accept Both Changes","둘 다 남기고 손으로 정리")],414,cols=3)
s.t(40,488,"<<<<<<< ======= >>>>>>> 표시가 하나도 남지 않게 정리하고 저장해야 합니다.",13,RED,700)
s.save("10-04")

# ============ 11장 ============
s=S(960,620,"File → Clone repository로 저장소를 받아 옵니다","그림 11-1")
s.r(40,84,250,200,"#fff",G,rx=6); s.r(40,84,250,34,"#F3F5F8",G,rx=6); s.o.append(f'<rect x="41" y="104" width="248" height="14" fill="#F3F5F8"/>')
for i,t in enumerate(["File","Edit","View","Repository"]): s.t(56+i*58,106,t,12,G,700 if i==0 else 400)
for i,t in enumerate(["New repository…","Add local repository…","Clone repository…","Options…"]):
    y=132+i*34
    if i==2: s.r(46,y,238,28,"#DCE3EC","#DCE3EC",rx=4)
    s.t(60,y+19,t,12.5,G,700 if i==2 else 400)
s.t(46,306,"Mac은 화면 맨 위 메뉴 막대의 File",11.5,MUTE)
callout(1,284,214)
appwin(330,84,590,380,"Clone a repository")
for i,t in enumerate(["GitHub.com","GitHub Enterprise","URL"]):
    tx=350+i*150; s.t(tx,166,t,13,G if i==2 else MUTE,700 if i==2 else 400)
    if i==2: s.o.append(f'<line x1="{tx-4}" y1="176" x2="{tx+34}" y2="176" stroke="{INK}" stroke-width="3"/>')
s.o.append('<line x1="330" y1="178" x2="920" y2="178" stroke="#C9D3DF"/>')
field(350,210,550,"Repository URL or GitHub username and repository","https://github.com/octocat/Spoon-Knife")
field(350,290,452,"Local path","C:\\GitHub\\Spoon-Knife",btn="Choose…",bw=90)
s.o.append('<line x1="330" y1="400" x2="920" y2="400" stroke="#C9D3DF"/>')
button(920-116,414,96,"Clone"); button(920-200,414,76,"Cancel",primary=False)
callout(2,700,160); callout(3,906,234); callout(4,330,314); callout(5,918,416)
legend_row([("File → Clone repository…","메뉴에서 고르기"),("URL 탭","주소로 받을 때"),("주소 붙여 넣기","브라우저 주소창의 주소"),("Local path 확인","작업 폴더 아래에 새 폴더로"),("Clone","받기 시작")],484,cols=3)
s.save("11-01")

s=S(960,480,"다른 PC에서 이어서 작업하기","그림 11-2")
s.r(40,110,240,150,"#fff",INK); s.t(60,146,"원래 PC",16,INK,700); s.t(60,176,"① 커밋하고 푸시",13.5,G,700); s.t(60,200,"Changes가 빈 상태로",12.5,MUTE)
s.r(360,110,240,150,TINT,INK); s.t(380,146,"GitHub",16,INK,700); s.t(380,176,"최신 기록이 모이는 곳",13.5,G,700)
s.r(680,110,240,150,"#fff",GRN); s.t(700,146,"다른 PC",16,GRN,700); s.t(700,176,"② 처음 한 번: Clone",13.5,G,700); s.t(700,200,"③ 그다음부터: Fetch · Pull",13.5,G,700); s.t(700,226,"작업 → 커밋 → 푸시",12.5,MUTE)
s.p("M282,170 L356,170"); s.t(319,160,"Push",12,INK,700,"middle")
s.p("M602,170 L676,170"); s.t(639,160,"Clone",12,INK,700,"middle")
s.p("M676,236 L602,236","g"); s.t(639,256,"Push",12,GRN,700,"middle")
s.p("M356,236 L282,236","g"); s.t(319,256,"Pull",12,GRN,700,"middle")
s.r(40,300,880,60,GRNT,GRN); s.t(60,336,"원래 PC로 돌아가면 작업 전에 Fetch → Pull. 두 PC 모두 \u201c시작할 때 받고, 끝날 때 올린다\u201d를 지키면 기록이 어긋나지 않습니다.",13.5,GRN,700)
s.t(40,408,"Clone은 GitHub의 저장소를 내 PC에 처음 통째로 받는 것, Pull은 이미 받은 저장소에 새 기록만 받는 것입니다.",13.5,MUTE)
s.save("11-02")

# ============ 12장 ============
s=S(960,470,"AI가 고치고, 사람이 확인하고 기록합니다","그림 12-1")
cols=[("AI 도구","파일 만들기·고치기","실행해 보기","바뀐 내용 설명하기",INK,"#fff"),("사람","커밋 전 세 가지 확인","커밋 메모 쓰기","커밋·푸시, PR, 병합",GRN,GRNT)]
for i,(t,a,b_,c,col,fl) in enumerate(cols):
    x=40+i*460
    s.r(x,90,420,250,fl,col); s.t(x+24,128,t,19,col,700)
    for k,l in enumerate((a,b_,c)): s.t(x+24,176+k*40,"· "+l,15,G)
s.p("M462,215 L496,215")
s.t(40,390,"AI 도구에 커밋·푸시까지 맡길 수도 있지만, 그 경우에도 커밋 전 확인은 사람이 합니다.",13.5,MUTE)
s.t(40,412,"확인 없이 기록된 커밋은 나중에 무엇이 잘못됐는지 찾기 어렵습니다.",13.5,MUTE)
s.save("12-01")

s=S(960,500,"커밋 전 세 가지 확인","그림 12-2")
items=[("예상하지 못한 파일이 바뀌지 않았나","Changes 목록을 봅니다. 시키지 않은 파일이\n있으면 커밋하지 말고 AI에게 이유를 묻습니다","Changes 목록"),
       ("요청한 대로 동작하나","파일을 열거나 실행해 봅니다.\n코드를 다 이해할 필요는 없습니다","직접 열어 보기"),
       ("민감한 자료가 섞이지 않았나","비밀번호, API 키, 개인정보,\n외부에 나가면 안 되는 자료","diff 훑어보기")]
for i,(a,b_,c) in enumerate(items):
    x=40+i*300
    s.r(x,90,270,280,"#fff",INK); s.b(x+30,124,i+1)
    s.t(x+56,130,c,13,MUTE,700)
    words=a
    s.t(x+22,178,a[:12],16,G,700); s.t(x+22,202,a[12:],16,G,700)
    for k,l in enumerate(b_.split("\n")): s.t(x+22,244+k*22,l,13,MUTE)
s.t(40,420,"셋 중 하나라도 걸리면 커밋하지 않습니다. 필요하면 7장의 Discard Changes로 버리고 다시 시킵니다.",13.5,G,700)
s.save("12-02")

s=S(960,520,".gitignore에 적은 파일은 Git이 무시합니다","그림 12-3")
s.r(40,90,300,300,"#fff",INK,rx=6); s.t(60,120,"my-first-repo 폴더",14,G,700)
for k,(n,c) in enumerate([(".gitignore",INK),("README.md",G),("회의록-양식.md",G),("비밀.txt",RED)]):
    s.o.append(f'<path d="M64,{146+k*44} h16 l8,8 v20 h-24 z" fill="#fff" stroke="{c}" stroke-width="2"/>'); s.t(100,164+k*44,n,14,c,700)
s.r(380,90,250,160,"#1E1E1E","#1E1E1E",rx=6); s.t(396,118,".gitignore",12.5,"#CCCCCC",700)
s.t(396,150,"비밀.txt",14,"#CE9178"); s.t(396,176,"*.env",14,"#CE9178"); s.t(396,202,"data/",14,"#CE9178")
s.t(396,236,"한 줄에 하나씩",11.5,"#9A9A9A")
X=670
s.r(X,90,250,300,"#fff",G,rx=6); s.t(X+16,118,"Changes",13.5,G,700)
check(X+16,138,".gitignore",True)
s.t(X+16,196,"비밀.txt 는",13,RED,700); s.t(X+16,218,"목록에 나타나지 않음",13,RED,700)
s.p("M340,300 C 480,330 560,300 668,210","r",dash="6 4")
s.t(40,432,"비밀.txt는 폴더에 있지만 Changes에 나타나지 않고, 커밋·푸시되지 않습니다. *는 '아무 이름'이라는 뜻으로,",13.5,MUTE)
s.t(40,454,"*.env는 이름이 .env로 끝나는 모든 파일, data/는 data 폴더 전체를 뜻합니다.",13.5,MUTE)
s.save("12-03")

# ============ 13장 ============
s=S(960,430,"매일 하는 순서","그림 13-1")
st=[("최신으로 맞추기","받기 + main 반영","Pull · Update from main"),("브랜치 확인","work인지 보기","Current Branch"),("작업","직접 또는 AI 도구로","VS Code · AI 도구"),("세 가지 확인","파일 · 동작 · 민감정보","Changes + 직접 실행"),("Commit → Push","한 줄 메모 쓰고 올리기","왼쪽 아래 · 위쪽 오른쪽")]
for i,(a,b_,c) in enumerate(st):
    x=34+i*182; s.r(x,96,164,150,"#fff",INK); s.b(x+28,126,i+1); s.t(x+16,170,a,15,G,700); s.t(x+16,194,b_,12.5,MUTE)
    s.o.append(f'<line x1="{x+16}" y1="212" x2="{x+148}" y2="212" stroke="{LINE}"/>'); s.t(x+16,232,c,11.5,INK,700)
    if i<4: s.p(f"M{x+165},171 L{x+180},171")
s.p("M844,246 L844,282 L116,282 L116,250","i",dash="5 4"); s.t(480,302,"다음에 작업할 때 다시 ①부터",13.5,INK,700,"middle")
s.r(34,322,892,52,GRNT,GRN); s.t(52,354,"한 덩어리가 완성되면  →  PR 만들기  →  검토  →  병합 (Create a merge commit)  →  main 받기",14.5,GRN,700)
s.save("13-01")
