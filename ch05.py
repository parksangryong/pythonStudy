# 1. 클래스 상속 받고 메서드 추가
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
    def div(self, val):
        self.value /= val
    def mul(self, val):
        self.value *= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
cal.div(2)
cal.mul(3)

print(cal.value)
print(f'='*20)

# 2. 클래스 상속 받고 메서드 추가2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
cal.add(80)

print(cal.value)
print(f'='*20)

# 3. 참과 거짓 예측하기
allBool = all([1,2,abs(-3)-3]) # False
print(allBool)

chrBool = chr(ord('a')) == 'a' # True
print(chrBool)

print(f'='*20)

# 4. 음수 제거하기(lambda, filter 사용)
data = [1, -2, 3, -5, 8, -3]

result = list(filter(lambda x: x > 0, data))
print(result)

print(f'='*20)

# 5. 16진수를 10진수로 변경하기
a = hex(234)
b= int(a, 16)
print(a, "->", b)

print(f'='*20)

# 6. 리스트 항목마다 곱하기 3
data = [1, 2, 3, 4]
result = list(map(lambda x: x * 3, data))
print(result)

print(f'='*20)

# 7. 최대값과 최소값의 합
data = [-8, 2, 7, 5, -3, 5, 0, 1]
max_value = max(data)
min_value = min(data)
print(max_value + min_value)

print(f'='*20)

# 8. 소수점 반올림하기
a = round(17/3, 4)
print(a)

print(f'='*20)

# 10. 파일 확장자가 .py 인 파일만 찾기
import glob

py_files = glob.glob("*.py")
print(py_files)

print(f'='*20)

# 11. 날짜 표시하기
import datetime

date = datetime.datetime.now()
formatDate= date.strftime("%Y/%m/%d %H:%M:%S")
print(formatDate)

print(f'='*20)

# 12. 로또 번호 생성기
import random

numbers = range(1, 46)
lotto = random.sample(numbers, 6)
print(lotto)

print(f'='*20)

# 13. 날짜 비교
date1 = datetime.date(1995, 11, 20)
date2 = datetime.date(1998, 10, 6)

diff = date1 - date2

print(str(abs(diff.days)) + "일")

print(f'='*20)

# 14. 기록순으로 정렬하기
from faker import Faker
import operator

fake = Faker('ko-KR')

data = [(fake.name(), round(random.random() * 17, 1)) for i in range(20)]
result = sorted(data, key=operator.itemgetter(1))
print(result)

print(f'='*20)

# 15. 청소당번 2명 뽑기
import itertools

students = [fake.name() for i in range(4)]
result = itertools.combinations(students, 2)
print(list(result))

print(f'='*20)

# 16. 문자열 나열하기
str1 = "abcd"
result = itertools.permutations(str1, 4)
# 튜플을 문자열로 합치기
permutations_list = [''.join(p) for p in result]
print(permutations_list)

print(f'='*20)

# 17. 5명에게 할 일 부여하기
students = ["김승현", "이영희", "박철수", "최민수", "정호영"]
suffle_students = random.sample(students, len(students))
jobs = ['청소', '빨래', '설거지']

result = itertools.zip_longest(suffle_students, jobs, fillvalue="휴식")
print(list(result))

print(f'='*20)

# 18. 벽에 타일 붙이기
import math

width = 200
height = 80

gcd = math.gcd(width, height)
result = (width * height) / (gcd * gcd)
print(str(result), "개")

print(f'='*20)

