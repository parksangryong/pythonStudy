# 8. 파일 역순으로 저장하기
f = open("abc.txt", "r")
lines = f.readlines()
f.close()

lines.reverse()

f = open("abc.txt", "w")
for line in lines:
    f.write(line)
f.close()

print("="*30)

# 9. 평균 구하기
f = open("sample.txt", "r")
lines = f.readlines()
f.close()

result = 0
for line in lines:
    result += int(line)

print(result / len(lines))

f = open("result.txt", "w")
f.write(str(result / len(lines)))
f.close()

print("="*30)
