# 1. 평균 점수 구하기
d1 = {'국어': 80, '영어': 75, '수학': 55}

avg = sum(d1.values()) / len(d1)
print("평균 점수는", avg, "점 입니다.")

print(f"{"":=^40}")

# 2. 짝수 홀수 구하기
num = 13
if(num %2 == 0):
    print(f"{num}은 짝수")
else:
    print(f"{num}은 홀수")

print(f"{"":=^40}")

# 3. 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(f"생년월일: {yyyymmdd}")
print(f"뒷자리: {num}")

print(f"{"":=^40}")

# 4. 주민등록번호 인덱싱(성별)
gender = num[0]
print(f"성별: {gender}")

print(f"{"":=^40}")

# 5. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

print(f"{"":=^40}")

# 6. 리스트 역순 정렬하기
c = [1,3,5,4,2]
c.sort()
c.reverse()
print(c)

print(f"{"":=^40}")

# 7. 리스트 문자열로 만들기
d = ['Life', 'is', 'too', 'short']
result = " ".join(d)
print(result)

print(f"{"":=^40}")

# 8. 튜플 더하기
e = (1,2,3)
f = e + (4,)
print(f)

print(f"{"":=^40}")

# 9. 딕셔너리 키 값 추가
g = dict()
print(g)

g['name'] = 'python'
g[('a',)] = 'python'
# g[[1]] = 'python'
g[250] = 'python'

print(g)

print(f"{"":=^40}")

# 10. 딕셔너리 값 추출
h = {'A':90, 'B':80, 'C':70}
result = h.pop('B')
print(h)
print(result)

print(f"{"":=^40}")

# 11. 리스트 중복 제거
i = [1,1,1,2,2,3,3,3,4,4,5]
iSet = set(i)
print(iSet)
j = list(iSet)
print(j)

print(f"{"":=^40}")

# 12. 파이썬 변수
k = l = [1,2,3]
k[1] = 4
print(l)
print(f"k의 주소: {id(k)}, l의 주소: {id(l)}")