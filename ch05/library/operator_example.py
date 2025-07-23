
import operator

# 튜플 정렬
students = [('홍길동', 3.9, 20230101), ('이순신', 3.0, 20230202), ('김철수', 4.3, 20230303)]

result = sorted(students, key=operator.itemgetter(1))
print(result)

# 딕셔너리 정렬
students = [
    {'name': '홍길동', 'score': 3.9, 'date': 20230101},
    {'name': '이순신', 'score': 3.0, 'date': 20230202},
    {'name': '김철수', 'score': 4.3, 'date': 20230303}
]

result = sorted(students, key=operator.itemgetter('score'))
print(result)

# 클래스 정렬
class Student:
    def __init__(self, name, score, date):
        self.name = name
        self.score = score
        self.date = date

students = [Student('홍길동', 3.9, 20230101), Student('이순신', 3.0, 20230202), Student('김철수', 4.3, 20230303)]

result = sorted(students, key=operator.attrgetter('score'))
print(result)