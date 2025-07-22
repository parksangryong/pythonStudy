class Family:
    firstname = "김"

    def __init__(self, name):
        self.name = name

    def getName(self):
        print(f"{self.firstname}{self.name}")

print(Family.firstname)
a = Family("철수")
b = Family("영희")

a.getName()
b.getName()

Family.firstname = "박"
print(Family.firstname)

a.getName()
b.getName()