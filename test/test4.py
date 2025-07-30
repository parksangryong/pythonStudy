# 10. 계산기 만들기
class Calculator:
    def __init__(self, nums):
        self.nums = nums
    def sum(self):
        return sum(self.nums)
    def avg(self):
        return sum(self.nums) / len(self.nums)

cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())

# 11. 모듈을 사용하는 방법
# mymod.py 모듈이 있다고 가정할 때, 이 모듈을 import 해서 사용할 수 있는 방법을 모두 기술하라
# import mymod 시 오류가 없어야함

# mymod.py에 add 함수와 PI 변수가 있다고 가정

# 1. 전체 모듈을 import
import mymod
print("1. import mymod:")
print(f"mymod.add(1,2) = {mymod.add(1,2)}")
print(f"mymod.PI = {mymod.PI}")
print()

# 2. 모듈의 모든 것을 import (기존 import들과 충돌을 피하기 위해 주석)
# from mymod import *
# print("2. from mymod import *:")
# print(f"add(1,2) = {add(1,2)}")
# print(f"PI = {PI}")
# print()

# 3. 특정 함수와 변수만 import
from mymod import add, PI
print("3. from mymod import add, PI:")
print(f"add(1,2) = {add(1,2)}")
print(f"PI = {PI}")
print()

# 4. 모듈을 별칭으로 import
import mymod as m
print("4. import mymod as m:")
print(f"m.add(1,2) = {m.add(1,2)}")
print(f"m.PI = {m.PI}")
print()

# 5. 특정 함수를 별칭으로 import
from mymod import add as plus
print("5. from mymod import add as plus:")
print(f"plus(1,2) = {plus(1,2)}")
print()