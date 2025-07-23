import os

# 환경 변수값 출력
print(os.environ)
print(os.environ['PATH'])

# 시스템 명령어 호출
os.system('dir')

# 실행한 시스템 명령어의 결과값 돌려받기
f = os.popen('dir')
print(f.read())

# 현재 디렉토리 출력
print(os.getcwd())

# 현재 디렉토리 변경
os.chdir('/Users')
print(os.getcwd())