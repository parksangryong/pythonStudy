import shutil
import glob
import pickle
import os

# 파일 만들기(객체 형태로 저장, wb로 열고 pickle로 저장)
f = open('test.txt', 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

# 파일 복사(같은 경로에)
shutil.copy('test.txt', 'test_copy.txt')

# 디렉토리가 존재하지 않으면 생성
if not os.path.exists('test_copy'):
    os.makedirs('test_copy')
    
# 그 경로에 무슨 파일이 있는지 파일 리스트 확인
files_in_test_copy = glob.glob("test_copy/*")
print(files_in_test_copy) # ['test_copy/test_copy.txt']

# 복사한 파일을 디렉토리로 이동
shutil.move('test_copy.txt', 'test_copy/test_copy.txt')

# 객체 형태 그대로 가져오기(rb로 열고 pickle로 읽기)
f = open('test.txt', 'rb')
data = pickle.load(f)
print(data) # {1: 'python', 2: 'you need'}