# 예제 1
def add_mul(choice, *args):   # string을 여러개 받으려면 **kwargs
		if choice == "add":
				result = 0
				for i in args:
						result = result + i
		elif choice == "mul":
				result = 1
				for i in args:
						result = result * i
		return result
		
result = add_mul("add", 1,2,3,4,5) # 15 (add 생략)
print(result)
result = add_mul("mul", 1,2,3,4,5) # 120
print(result)

print(f"{"":=^30}")

# 예제2
def say_myself(name, age, man=True):
		print(f"나의 이름은 {name}입니다.")
		print(f"나의 나이는 {age}입니다.")
		if(man):
				print("남자입니다")
		else:
				print("여자입니다")

say_myself("홍길동", 23)
say_myself("홍길순", 22, False)

print(f"{"":=^30}")

# 1. 홀수 짝수 판별하기
def is_odd(number):
    if number % 2 == 0:
        print("짝수")
    else:
        print("홀수")

is_odd(3)
is_odd(4)

print(f"{"":=^30}")

# 2. 평균 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result = result + i
    return result / len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

print(f"{"":=^30}")

# 3. 프로그램 오류 수정
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print(f"두 수의 합은 {total}입니다")

print(f"{"":=^30}")

# 4. 출력 테스트
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

print(f"{"":=^30}")

# 5. 프로그램 오류 수정
# f1 = open("test.txt", "w")
# f1.write("Life is too short\n")
# f1.close()

# f2 = open("test.txt", "r")
# print(f2.read()) 
# f2.close()

# print(f"{"":=^30}")

# 6. 사용자 입력 저장
# user_input = input("저장할 내용을 입력하세요:")
# f = open('test.txt', 'a')
# f.write(user_input)
# f.write("\n")
# f.close()

# print(f"{"":=^30}")

# 7. 파일의 문자열 바꾸기
f = open("test.txt", "r")
body = f.read()
f.close()

body = body.replace("java", "python")

f = open("test.txt", "w")
f.write(body)
f.close()