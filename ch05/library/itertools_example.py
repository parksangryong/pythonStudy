import itertools

students = ['한민서', '이철수', '조민지', '조아라', '김민지']
snack = ['사탕', '초콜릿', '젤리']

result = itertools.zip_longest(students, snack, fillvalue='새우깡')
print(list(result))


list(itertools.permutations(['1', '2', '3'], 2))
print(list(itertools.permutations(['1', '2', '3'], 2)))

list(itertools.combinations(['1', '2', '3'], 2))
print(list(itertools.combinations(['1', '2', '3'], 2)))