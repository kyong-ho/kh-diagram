"""한 과정의 그림 스크립트를 모두 실행한다.

    python3 scripts/figures/build.py <과정 폴더 이름 또는 경로>

FIG_OUT=<폴더> 를 주면 course.py가 정한 폴더 대신 그 폴더에 쓴다(비교·시험용).
"""
import glob, os, runpy, sys

if len(sys.argv)!=2: sys.exit(__doc__)
folder=os.path.join(os.path.dirname(os.path.abspath(__file__)),sys.argv[1])
if not os.path.isfile(os.path.join(folder,'course.py')): sys.exit(f"course.py가 없습니다: {folder}")
sys.path.insert(0,folder)
for path in sorted(glob.glob(os.path.join(folder,'*.py'))):
    if os.path.basename(path)!='course.py': runpy.run_path(path,run_name='__main__')
