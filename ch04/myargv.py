import sys

args = sys.argv[1:]

result = 0
for i in args:
    result = result + int(i)
print(result)