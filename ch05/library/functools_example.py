import functools

data = [1, 2, 3, 4, 5]

result = functools.reduce(lambda x, y: x + y, data)
print(result)