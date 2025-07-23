try:
    a = [1,2,3]
    print(a[3])
    print(10/0)
except ZeroDivisionError:  # 예외 처리
    print("0으로 나눌 수 없습니다.")
except IndexError:  # 예외 처리
    print("인덱스 범위를 벗어났습니다.")
except Exception as e:  # 예외 처리
    print(e)
finally:  # 예외 처리 후 실행
    print("finally")
