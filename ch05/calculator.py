# 클래스 선언
class Calculator:
    # 생성자
    def __init__(self):
        self.result = 0

    # 메서드 더하기 
    def add(self, num):
        self.result += num
        return self.result

    # 메서드 빼기
    def sub(self, num):
        self.result -= num
        return self.result

# 인스턴스 생성
# cal1 = Calculator()
# cal2 = Calculator()

# 메서드 호출
# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))