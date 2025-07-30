# 12. 오류와 예외처리
from traceback import print_tb


result = 0

try: 
    [1, 2, 3][3] # index error
    "a" + 1 # type error
    4 / 0 # zero division error
except TypeError:
    print("TypeError")
    result += 1
except ZeroDivisionError:
    print("ZeroDivisionError")
    result += 2
except IndexError:
    print("IndexError")
    result += 3
finally:
    result += 4

print(result)

print("-"*30)

# 13. DashInsert 함수
def DashInsert(num):
    result = ""
    for i in range(len(num)):
        if i > 0:
            if int(num[i]) % 2 == 1 and int(num[i-1]) % 2 == 1:
                result += "-"
            if int(num[i]) % 2 == 0 and int(num[i-1]) % 2 == 0:
                result += "*"
        result += num[i]
    return result

print(DashInsert("4546793"))
print("-"*30)

# 14. 문자열 압출하기
def compress_string(s):
    result = ""
    count = 1
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i+1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1
    return result

print(compress_string("aaabbcccccca"))
print("-"*30)

# 15. Duplicate Numbers
def chkDupNum(nums):
    result = []
    buffer = []

    numsArray = nums.split(" ")

    for num in numsArray:
        for i in range(0, 10):
            if num.count(str(i)) == 1:
                buffer.append("True")
            else:
                buffer.append("False")
        
        if "False" in buffer:
            result.append("False")
        else:
            result.append("True")
        
        buffer = []
    
    return " ".join(result)

print(chkDupNum("0123456789 01234 01234567890 6789012345 012322456789"))
print("-"*30)

# 16. 모스 부호 해독
def decoding(s):
    morse_dict = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---" : "O",
        ".--." : "P",
        "--.-" : "Q",
        ".-." : "R",
        "..." : "S",
        "-" : "T",
        "..-" : "U",
        "...-" : "V",
        ".--" : "W",
        "-..-" : "X",
        "-.--" : "Y",
        "--.." : "Z",
    }
    result = ""
    for word in s.split("  "):
        for char in word.split(" "):
            result += morse_dict[char]
        result += " "
    return result

print(decoding(".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"))