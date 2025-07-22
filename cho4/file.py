with open('foo.txt', 'w') as f:
		f.write("Lift is too sort, you need python")

with open('num.txt', 'w') as f:
    for i in range(1,11):
        data = f"{i}번째 줄입니다\n"
        f.write(data)