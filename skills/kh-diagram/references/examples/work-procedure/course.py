"""AI 업무 절차서 가이드 그림의 과정 설정."""
import os, sys, tempfile
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HERE,'..','..','..','scripts'))  # 스킬의 scripts/figlib.py
from figlib import *

setup(course="AI 업무 절차서 가이드",out=os.path.join(tempfile.gettempdir(),'figure-examples','work-procedure'))  # 보기용. 실제 비교는 verify_examples.py
