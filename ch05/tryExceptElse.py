try:
    age = int(input("나이를 입력하세요: "))
except:
        print("잘못된 값을 입력하였습니다.")
else:
    if age <= 18:
        print("미성년자는 출입할 수 없습니다.")
    else:
        print("환영합니다.")
finally:
    print("finally")
