import random

target = random.randint(1, 100)
count = 0

while True:
    answer = int(input("1~100 사이의 숫자를 입력하세요: "))
    count += 1

    if (answer) == target:
        print(f"정답입니다. {count}번 만에 맞췄습니다.")
        break
    elif (answer) < target:
        print("업 UP!")
    else:
        print("다운 DOWN!")
