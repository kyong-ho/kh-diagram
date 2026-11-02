"""리서치 글 본문 그림의 설정. 그림 파일 이름은 `<글 주소>-순번`으로 짓는다."""
import os, sys, tempfile
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HERE,'..','..','..','scripts'))  # 스킬의 scripts/figlib.py
from figlib import *

setup(course="리서치",out=os.path.join(tempfile.gettempdir(),'figure-examples','research'))  # 보기용. 실제 비교는 verify_examples.py
