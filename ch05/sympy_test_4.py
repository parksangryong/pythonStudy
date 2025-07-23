# 연립 방정식 풀기
import sympy
from fractions import Fraction

x, y = sympy.symbols('x, y')

f1 = sympy.Eq(x**2 + y, 20)
f2 = sympy.Eq(x - Fraction(1, 4) * y, 3)

result = sympy.solve([f1, f2])
print(result)