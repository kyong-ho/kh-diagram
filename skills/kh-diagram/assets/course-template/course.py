"""이 과정(또는 글 묶음) 그림의 설정. 아래 두 값만 고친다."""
import os, sys
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HERE,'..'))  # scripts/figures/figlib.py
from figlib import *

# course: 표제란에 적을 과정 이름.
# out: SVG를 쓸 폴더. 기본값은 프로젝트 루트의 figures-out/<이 폴더 이름>이고, 문서가 그림을 읽는 폴더로 바꾼다.
setup(course="내 과정 이름",out=os.path.join(HERE,'..','..','..','figures-out',os.path.basename(HERE)))
