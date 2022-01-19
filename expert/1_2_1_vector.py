# __repr__(), __abs__(), __add__(), __mul__()
# 특별 메서드를 이용해서 Vector 연산을 하는 클래스를 정의해보자
from math import hypot


class Vector():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# 특별 메서드를 구현하면 사용자 정의 객체도
# 내장형 객체처럼 작동하게 되어, 파이썬 스러운
# 표현력 있는 코딩 스타일을 구사할 수 있다.