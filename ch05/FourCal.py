class FourCal:
    # 생성자
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    # 메서드 설정
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # 메서드 더하기
    def add(self):
        return self.num1 + self.num2

    # 메서드 빼기
    def sub(self):
        return self.num1 - self.num2

    # 메서드 곱하기
    def mul(self):
        return self.num1 * self.num2

    # 메서드 나누기
    def div(self):
        return self.num1 / self.num2

# a = FourCal()
# a.setdata(13, 5)
# print(f"a.num1: {a.num1}")
# print(f"a.num2: {a.num2}")
# print(f"a.add(): {a.add()}")
# print(f"a.sub(): {a.sub()}")
# print(f"a.mul(): {a.mul()}")
# print(f"a.div(): {a.div()}")