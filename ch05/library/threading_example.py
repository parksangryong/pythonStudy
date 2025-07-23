import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"working: {i}")

print("start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task) # 스레드 생성
    threads.append(t)

for t in threads:
    t.start() # 스레드 시작

for t in threads:
    t.join() # 스레드 종료

print("end")