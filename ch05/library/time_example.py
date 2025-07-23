import time

time.time()
print(time.time())

time.localtime()
print(time.localtime())
print(time.localtime().tm_year)
print(time.localtime().tm_mon)
print(time.localtime().tm_mday)
print(time.localtime().tm_hour)
print(time.localtime().tm_min)
print(time.localtime().tm_sec)
print(time.localtime().tm_wday)
print(time.localtime().tm_yday)

time.asctime(time.localtime(time.time()))
print(time.asctime())

time.ctime()
print(time.ctime())

# strptime은 문자열을 시간 객체로 변환
time_str = time.strftime("%x", time.localtime(time.time()))
print(time_str)
time_str = time.strftime("%c", time.localtime(time.time()))
print(time_str)

time.mktime(time.localtime())
print(time.mktime(time.localtime()))

time.sleep(1)
print(time.sleep(1))