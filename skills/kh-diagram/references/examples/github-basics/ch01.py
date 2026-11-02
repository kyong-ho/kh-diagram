# GitHub 기초 가이드 1장(개념 만화) 그림.
from course import *
W,H=960,480

# 1
p=P(1,"고칠 때마다 파일이 늘어납니다","어느 게 최신인지, 누가 무엇을 고쳤는지 아무도 모릅니다.")
p.person(130,210,"sad"); p.bubble(190,96,190,50,["어느 게 진짜지…?"],(166,190))
for (x,y,r,l) in [(430,50,-7,"보고서_최종.hwp"),(570,62,5,"보고서_최종2.hwp"),(745,48,-4,"보고서_진짜최종.hwp"),(480,210,6,"보고서_최종_수정.hwp"),(670,214,-5,"보고서_진짜최종_0917.hwp")]:
    p.doc(x,y,rot=r,label=l)
p.save("1-01")
# 2
p=P(2,"Git은 내 폴더 안에 사는 '기록 담당'입니다","파일은 하나만 두면 됩니다. 내가 도장을 찍을 때마다 그때까지 바뀐 내용이 기록됩니다.")
p.person(120,200)
p.add(f'<path d="M220,72 h150 l22,28 h220 v250 h-392 z" fill="{AMBT}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'); p.t(238,94,"내 프로젝트 폴더",14,INK,700)
p.doc(262,160,84,106,label="보고서 (하나만!)"); git(460,225,1.25)
p.bubble(640,110,290,76,["도장을 찍어 주시면, 그때까지","바뀐 내용을 적어 둘게요."],(510,200))
p.save("1-02")
# 3
p=P(3,"커밋 = '여기까지 저장' 도장","도장을 찍을 때마다, 나중에 돌아올 수 있는 지점이 하나씩 생깁니다.")
p.person(120,215); p.bubble(84,78,170,48,["여기까지 저장!"],(128,178))
git(300,240); p.dots(350,890,240,[(440,INK),(600,INK),(760,INK)])
for x,l,tm in [(440,"표 추가","월 10:20"),(600,"오타 수정","월 11:05"),(760,"그래프 추가","화 09:40")]:
    p.add(f'<rect x="{x-58}" y="268" width="116" height="52" rx="10" fill="#fff" stroke="{LINE}" stroke-width="2"/>'); p.t(x,290,l,15,G,700,"middle"); p.t(x,310,tm,12.5,MUTE,400,"middle")
p.stamp(800,150,"여기까지",r=46,size=17); p.arrow("M785,196 L768,222","r",sw=3)
p.save("1-03")
# 4
p=P(4,"실수한 기록은 '취소 도장'으로 되돌립니다","기록을 지우는 것이 아니라, 그 변경을 취소하는 도장을 하나 더 찍습니다. 그래서 AI에게 부담 없이 시킬 수 있습니다.")
p.person(100,190); p.dots(180,880,240,[(250,INK),(390,INK),(530,INK),(670,RED),(810,GRN)])
for x,l in [(250,"표 추가"),(390,"오타 수정"),(530,"그래프 추가")]: p.t(x,282,l,14.5,G,700,"middle")
p.doc(638,268,64,80,broken=True); p.t(626,314,"망가짐",14.5,RED,700,"end")
p.t(810,282,"취소 도장",14.5,GRN,700,"middle"); p.t(810,302,"(되돌리기)",13,MUTE,700,"middle")
p.robot(560,96,0.9,None); p.bubble(626,36,250,48,["앗, 표를 망가뜨렸어요"],(600,84))
p.arrow("M800,218 C 786,156 700,156 680,214","r",dash="9 7"); p.t(742,146,"이 변경만 취소",16,RED,700,"middle")
p.save("1-04")
# 5
p=P(5,"그런데 Git의 기록은 내 PC 안에만 있습니다","PC가 고장 나면 기록도 함께 사라집니다. 다른 사람도 볼 수 없습니다.")
p.person(130,200,"wow"); p.pc(300,60,320,210,REDT); git(400,165,1.1,"sad"); p.dots(460,590,165,[(490,INK),(540,INK)],sw=4)
p.add(f'<path d="M520,60 L490,120 L535,135 L500,205 L545,215 L520,270" fill="none" stroke="{RED}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>')
p.stamp(640,80,"고장!",r=38,rot=14,size=18)
p.bubble(680,150,240,76,["제 기록은","이 PC 안에만 있는데요…"],(622,190))
p.save("1-05")
# 6
p=P(6,"GitHub는 그 기록을 올려 두는 온라인 보관함입니다","올리기는 '푸시', 받기는 '풀'입니다. 비공개로 만들면 내가 허락한 계정만 볼 수 있습니다.")
p.pc(70,80,280,190); git(150,175); p.dots(205,325,175,[(235,INK),(290,INK)],sw=4); p.t(210,316,"내 PC",16,INK,700,"middle")
p.cloud(735,160,1.55,"GitHub"); p.dots(690,810,215,[(720,GRN),(775,GRN)],GRN,4)
p.arrow("M375,140 L575,140","g",sw=5); p.t(475,122,"푸시 = 올리기",18,GRN,700,"middle")
p.arrow("M575,215 L375,215","i",sw=5); p.t(475,250,"풀 = 받기",18,INK,700,"middle")
p.lock(690,300); p.t(716,314,"비공개: 허락한 계정만",15,GRN,700)
p.save("1-06")
# 7
p=P(7,"이름은 비슷하지만 다른 것입니다","Git은 기록하는 도구이고, GitHub는 그 기록을 보관하는 곳입니다.")
p.add(f'<g clip-path="url(#c)"><rect x="0" y="0" width="480" height="{H-96}" fill="{AMBT}"/></g><rect x="4" y="4" width="952" height="472" rx="18" fill="none" stroke="{INK}" stroke-width="2.5"/>')
p.add(f'<circle cx="46" cy="46" r="21" fill="{INK}"/>'); p.t(46,53,"7",19,"#fff",700,"middle")
p.add(f'<line x1="480" y1="4" x2="480" y2="{H-96}" stroke="{INK}" stroke-width="2" stroke-dasharray="7 6"/><circle cx="480" cy="190" r="30" fill="#fff" stroke="{INK}" stroke-width="3"/>'); p.t(480,201,"≠",30,INK,700,"middle")
git(240,120,1.35); p.t(240,232,"Git",32,INK,700,"middle"); p.t(240,270,"내 PC 안에 있습니다",17,G,400,"middle"); p.t(240,298,"변경 이력을 기록하는 도구",17,G,700,"middle"); p.t(240,326,"인터넷이 없어도 돌아갑니다",17,G,400,"middle")
p.cloud(712,112,1.25,""); p.t(720,232,"GitHub",32,GRN,700,"middle"); p.t(720,270,"인터넷에 있습니다",17,G,400,"middle"); p.t(720,298,"기록을 보관하고 함께 보는 곳",17,G,700,"middle"); p.t(720,326,"PC가 고장 나도 남습니다",17,G,400,"middle")
p.save("1-07")
# 8
p=P(8,"초안에서 마음껏 고치고, 검토를 거쳐 최종본으로","합쳐 달라는 요청을 PR, 실제로 합치는 것을 병합이라고 합니다. work는 이 튜토리얼에서 쓰는 이름입니다.")
def tag(x,y,name,col):
    p.add(f'<path d="M{x+12},{y} h86 a6,6 0 0 1 6,6 v20 a6,6 0 0 1 -6,6 h-86 l-12,-16 z" fill="#fff" stroke="{col}" stroke-width="2.5" stroke-linejoin="round"/><circle cx="{x+14}" cy="{y+16}" r="3" fill="{col}"/>')
    p.t(x+60,y+22,name,17,col,700,"middle")
p.t(62,106,"초안",24,INK,700); tag(58,120,"work",INK); p.dots(200,560,120,[(250,INK),(340,INK),(430,INK),(520,INK)])
p.t(62,306,"최종본",24,GRN,700); tag(58,320,"main",GRN); p.dots(200,860,320,[(320,GRN),(680,GRN)],GRN); p.lock(900,314)
p.arrow("M536,120 H680 V296","i",sw=4); p.t(612,104,"결재 올리기 (PR)",16,INK,700,"middle")
p.stamp(680,195,"승인",r=34,size=18); p.t(696,268,"병합",15,INK,700); p.person(810,140,"smile",0.72,label="검토")
p.save("1-08")
# 9
p=P(9,"AI 도구와 함께 쓸 때: AI가 고치고, 나는 확인하고 도장을 찍습니다","AI가 여러 파일을 바꿔도 무엇이 바뀌었는지 볼 수 있습니다. 결과를 확인하는 일은 사람이 합니다.")
for i,(x,l) in enumerate([(70,"AI가 파일을 고친다"),(360,"내가 결과를 확인한다"),(650,"도장 찍고 올린다")]):
    p.add(f'<rect x="{x}" y="70" width="240" height="270" rx="16" fill="#fff" stroke="{LINE}" stroke-width="2.5"/><circle cx="{x+30}" cy="312" r="14" fill="{INK}"/>'); p.t(x+30,317,str(i+1),15,"#fff",700,"middle"); p.t(x+52,318,l,15.5,G,700)
    if i<2: p.arrow(f"M{x+250},200 L{x+280},200",sw=4)
p.robot(150,170); p.doc(210,120,64,80)
p.person(440,140,"smile",0.85); p.doc(510,120,70,90,diff=True)
p.stamp(730,200,"여기까지",r=42,size=16); p.cloud(820,130,0.62,""); p.arrow("M775,185 L800,160","g",sw=4)
p.save("1-09")
# 10
p=P(10,"기억할 것은 세 가지뿐입니다","받기 → 작업 → 도장 찍기 → 올리기. 나머지는 해 보면서 익히면 됩니다.")
for x,a,b,when,col in [(200,"받기","풀 (pull)","작업 시작할 때 (받을 것이 있으면)",INK),(480,"도장 찍기","커밋 (commit)","한 덩어리가 끝날 때마다",RED),(760,"올리기","푸시 (push)","도장 찍은 뒤, 하루를 마칠 때",GRN)]:
    p.add(f'<circle cx="{x}" cy="205" r="100" fill="{ {INK:TINT,RED:REDT,GRN:GRNT}[col] }" stroke="{col}" stroke-width="3.5"/>')
    p.t(x,238,a,26,col,700,"middle"); p.t(x,266,b,15.5,MUTE,700,"middle"); p.t(x,82,when,15,G,700,"middle")
p.arrow("M200,130 L200,178","i",sw=7); p.stamp(480,158,"",r=24,rot=-12); p.arrow("M760,182 L760,134","g",sw=7)
p.arrow("M308,205 L372,205",sw=4); p.arrow("M588,205 L652,205",sw=4)
p.save("1-10")
