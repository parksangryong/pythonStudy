# 1. 문자열 바꾸기
# 1-1
str = "a:b:c:d"
str = str.replace(":","#")
print(str)

# 1-2
str = "a:b:c:d"
str = str.split(":")
str = "#".join(str)
print(str)

print("="*30)

# 2. 딕셔너리 값 추출하기 (에러 대신 값 출력)
a = {'A':90, 'B':80}
print(a.get('C', 70))

print("="*30)

# 3. 리스트 더하기와 extend 함수
a = [1,2,3]
a = a + [4,5] 
# 기존 리스트와 새 리스트 합쳐 새 리스트 객체 생성
# 느리고 많은 메모리 쓰며 원본이 보장됨
print(a)

a = [1,2,3]
a.extend([4,5])
# 기존 리스트 객체를 직접 수정
# 빠르고 메모리 효율적이며 원본이 변경됨
print(a)

print("="*30)

# 4. 리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0
for i in A:
    if i >= 50:
        result += i
print(result)

print("="*30)

# 5. 피보나치 함수
def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        result = [0, 1]
        for i in range(2, n):
            result.append(result[i-1] + result[i-2])
        return result

input_num = int(input("피보나치 수열의 항 수를 입력하세요: "))
print(fib(input_num))

print("="*30)
