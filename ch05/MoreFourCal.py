from FourCal import FourCal

class MoreFourCal(FourCal):
    def pow(self):
        return self.num1 ** self.num2

    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2

cal = MoreFourCal()
cal.setdata(14, 0)
print(f"cal.add(): {cal.add()}")
print(f"cal.sub(): {cal.sub()}")
print(f"cal.mul(): {cal.mul()}")
print(f"cal.div(): {cal.div()}")
print(f"cal.pow(): {cal.pow()}")