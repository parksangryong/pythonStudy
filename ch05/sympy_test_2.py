# 2차 방정식 풀기
import sympy

x = sympy.Symbol('x')
f = sympy.Eq(x**2, 1)

result = sympy.solve(f)
print(result)