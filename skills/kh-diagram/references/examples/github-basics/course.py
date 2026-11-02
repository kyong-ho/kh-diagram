"""GitHub 기초 가이드 그림의 과정 설정과 이 과정에서만 쓰는 부품."""
import os, sys, tempfile
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HERE,'..','..','..','scripts'))  # 스킬의 scripts/figlib.py
from figlib import *

setup(course="GitHub 튜토리얼",out=os.path.join(tempfile.gettempdir(),'figure-examples','github-basics'))  # 보기용. 실제 비교는 verify_examples.py

def git(x,y,k=1.0,mood="smile"):
    """1장 만화의 'Git' 수첩 캐릭터."""
    m={"smile":"M-2,8 Q7,16 16,8","sad":"M-2,14 Q7,6 16,14"}[mood]
    rings=''.join(f'<circle cx="-24" cy="{yy}" r="3.5" fill="#fff" stroke="{INK}" stroke-width="2"/>' for yy in(-26,-9,8,25))
    cur().o.append(f'<g transform="translate({x},{y}) scale({k})"><rect x="-34" y="-42" width="68" height="84" rx="9" fill="{AMB}" stroke="{INK}" stroke-width="3"/>{rings}<circle cx="-1" cy="-10" r="3.2" fill="{G}"/><circle cx="15" cy="-10" r="3.2" fill="{G}"/><path d="{m}" fill="none" stroke="{G}" stroke-width="2.5" stroke-linecap="round"/><text x="7" y="33" font-size="14" font-weight="700" fill="{INK}" text-anchor="middle">Git</text></g>')

def desktop(x,y,w,h,branch="main",action="Fetch origin",action_sub="Last fetched just now",tab="Changes"):
    """GitHub Desktop 창. 왼쪽 목록 칸의 폭을 돌려준다."""
    s=cur()
    s.r(x,y,w,h,"#fff",G,rx=8)
    s.r(x,y,w,52,"#2B3138",G,rx=8); s.o.append(f'<rect x="{x+1}" y="{y+36}" width="{w-2}" height="16" fill="#2B3138"/>')
    cw=w/3
    for i,(l1,l2) in enumerate((("Current Repository","my-first-repo"),("Current Branch",branch),(action,action_sub))):
        bx=x+i*cw; s.t(bx+16,y+22,l1,10.5,"#AEB8C4"); s.t(bx+16,y+41,l2,13,"#fff",700)
        if i: s.o.append(f'<line x1="{bx}" y1="{y}" x2="{bx}" y2="{y+52}" stroke="#4A525C"/>')
    lw=250
    s.o.append(f'<line x1="{x+lw}" y1="{y+52}" x2="{x+lw}" y2="{y+h}" stroke="{LINE}" stroke-width="1.5"/>')
    for i,t in enumerate(("Changes","History")):
        tx=x+20+i*120; s.t(tx+20,y+78,t,13.5,G if t==tab else MUTE,700 if t==tab else 400)
        if t==tab: s.o.append(f'<line x1="{tx}" y1="{y+89}" x2="{tx+100}" y2="{y+89}" stroke="{INK}" stroke-width="3"/>')
    s.o.append(f'<line x1="{x}" y1="{y+90}" x2="{x+lw}" y2="{y+90}" stroke="{LINE}"/>')
    return lw
