try:
    input_num = int(input("숫자를 입력하세요: "))
except ValueError:
    print("숫자만 입력할 수 있습니다.")
    exit()
else:
    if input_num < 1 or input_num > 999:
        print("1~999 사이의 숫자만 입력 가능합니다.")
        exit()

result = 0
for i in range(1, input_num + 1):
    if i % 3 == 0:
        result += i
    elif i % 5 == 0:
        result += i

print(result)
