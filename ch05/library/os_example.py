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

# 디렉터리 생성
os.mkdir('test')

# 디렉터리 삭제
os.rmdir('test')

# 디렉터리 목록 출력
print(os.listdir())

# 디렉터리 존재 여부 확인
print(os.path.exists('test'))

# 파일 존재 여부 확인
print(os.path.exists('test.txt'))

# 파일 크기 확인
print(os.path.getsize('test.txt'))

# 파일 이름 변경
os.rename('test.txt', 'test_copy.txt')

# 파일 삭제
os.remove('test_copy.txt')