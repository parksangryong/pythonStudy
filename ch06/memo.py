import os

class Memo:
    def __init__(self, memo_name):
        self.memo_name = memo_name
        if not os.path.exists(self.memo_name + '.txt'):
            with open(self.memo_name + '.txt', 'w') as f:
                f.write('')

    def write_memo(self, memo):
        with open(self.memo_name + '.txt', 'a') as f:
            f.write(memo + '\n')

    def read_memo(self):
        with open(self.memo_name + '.txt', 'r') as f:
            print(f.read())

memo_name = input("메모 파일 이름을 입력하세요: ")
memo = Memo(memo_name)

while True:
    print(f'='*20)
    print("1. 메모 쓰기")
    print("2. 메모 읽기")
    print("3. 메모 종료")
    print(f'='*20)

    choice = input("사용할 기능을 선택하세요: ")

    if choice == '1':
        memo.write_memo(input("메모를 입력하세요: "))
    elif choice == '2':
        memo.read_memo()
    elif choice == '3':
        print("메모 종료")
        break