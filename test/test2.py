# 6. 숫자의 총합 구하기
input_num = input("숫자를 입력하세요(,로 구분): ")
input_num = input_num.split(",")
result = 0

for i in input_num:
    result += int(i)
print(result)

print("="*30)

# 7. 한 줄 구구단
input_num = int(input("구구단을 출력할 숫자를 입력하세요: "))
result = []
for i in range(1, 10):
    result.append(input_num * i)
    
for i in result:
    print(i, end=" ")
print()

print("="*30)
