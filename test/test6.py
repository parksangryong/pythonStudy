# 17. 정규식 기초문자
import re

p = re.compile('a[.]{3,}b')
# a +  . 3개 이상 + b

print(p.match("acccb"))
print(p.match("a....b"))
print(p.match("aaab"))
print(p.match("a.cccb"))
print(p.search('hello a......b world')) 

print("-"*30)

# 18. 정규식 문자열 검색
import re

p = re.compile("[a-z]+")
m = p.search("3 python")

m.start() + m.end()

print(m)
print(m.start())
print(m.end())
print(m.start() + m.end())

print("-"*30)

# 19. 정규식 그루핑
import re

# 휴대폰 번호 뒷자리 4개를 #### 으로 바꾸는 프로그램을 정규식으로 작성
def mask_phone_number(phone_number):
    return re.sub(r'\d{4}$', '####', phone_number)
    # \d{4} : 뒷자리 4개
    # $ : 뒷자리
    # re.sub : 문자열 치환

print(mask_phone_number("park 010-1234-5678"))
print(mask_phone_number("kim 010-1234-5678"))
print(mask_phone_number("lee 010-1234-5678"))

print("-"*30)