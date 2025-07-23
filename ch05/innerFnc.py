for i, name in enumerate(['body', 'foo', 'bar']):
		print(i, name)

a = list(zip([1,2,3], ['a', 'b', 'c']))
b = list(zip([1,2,3], ['a', 'b', 'c', 'd']))
c = list(zip([1,2,3], ['a', 'b', 'c', 'd'], ['x', 'y', 'z']))
d = list(zip('abc', 'def', 'ghi'))
print(a)
print(b)
print(c)
print(d)
