# 1차 방정식 풀기
import sympy
from fractions import Fraction

# 가지고 있는 돈 x (잔액)
x = sympy.Symbol('x')

# 가지고 있던 돈의 2/5가 1760원 (소비)
f = sympy.Eq(x * Fraction(2, 5), 1760)

# 전체 금액 값은?
result = sympy.solve(f)
print(result)

# 현재 x 값은?
remains = result[0] - 1760
print(f'현재 가지고 있는 돈은 {remains}원 입니다.')