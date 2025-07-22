# 0. 나무 찍기
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:
        print("나무가 넘어갑니다.")

print(f"{"":=^20}")

# 0. 1~10 중 3의 배수를 뺀 나머지 값 출력
num = 0
while True:
    num = num + 1
    if num % 3 == 0:
        continue
    if num > 10:
        break
    print(num)

print(f"{"":=^20}")

# 0. 시험 합격여부
marks = [90, 25, 67, 45, 80]

for mark in marks:
    if mark <= 60:
        continue
    print(f"{mark}점은 합격입니다.")

print(f"{"":=^20}")

# 0. 1~100 합
add = 0
for i in range(1, 101):
    add = add + i
print(add)

print(f"{"":=^20}")

# 0. 구구단
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")
    print(f"{"":=^20}")

# 1. 조건문의 참과 거짓
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

print(f"{"":=^20}")

# 2. 3의 배수의 합 구하기
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

print(f"{"":=^20}")

# 3. 별 표시하기
i = 0
while True:
    i += 1
    if i > 5: break
    print("*" * i)

print(f"{"":=^20}")

# 4. 평균 점수 구하기
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
avg = total / len(A)
print(avg)

print(f"{"":=^20}")

# 5. 리스트 컴프리헨션
numbers = [1,2,3,4,5]
result = [item*2 for item in numbers if item % 2 == 1]
print(result)

print(f"{"":=^20}")

