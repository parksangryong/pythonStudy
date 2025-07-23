import datetime

day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023,4,5)

diff = day2 - day1
print(diff)

today = datetime.date.today()
print(today)

# 요일 출력
print(day1.weekday())

# 요일 출력
print(day1.isoweekday())

# 주차 출력
print(day1.isocalendar())

# 날짜 출력
print(day1.isoformat())

# 날짜 출력
print(day1.strftime("%Y-%m-%d %H:%M:%S"))