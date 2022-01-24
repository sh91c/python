"""
    재귀함수
"""

"""
    재귀함수: 함수가 자기 자신을 호출.
    파이썬에서 재귀가 깊다면 예외가 발생.
"""

# def dive():
#     return dive()
#
#
# dive()  # RecursionError: maximum recursion depth exceeded

"""
    재귀 함수의 깊이를 제한을 알고 설정이 가능함.
"""
# import sys
#
# print(sys.getrecursionlimit())  # 1000으로 제한되어있다.
# sys.setrecursionlimit(500)  # 500으로 set 가능

"""
    리스트의 리스트의 리스트와 같이 flatten 하지 않은 데이터를 처리할 때 유용
    (= 시퀀스의 시퀀스를 하나의 시퀀스로 수집하기와 같은 면접 질문 예상 가능)
"""


# flatten 함수의 인자로 고르지 않은 리스트를 활용
def flatten(lol):
    for item in lol:  # 반복문을 통해 각 아이템의 타입을
        if isinstance(item, list):  # 리스트인지 비교한다. # 리스트라면 재귀 호출을 하여 다시 반복문을 통해 값을 꺼내어 비교한다. 계속해서 리스트라면 재귀호출을 할 것이다.
            yield from flatten(item)  # yeild from 표현식*
        else:  # 해당 아이템의 타입이 리스트가 아니라면 yield item을 진행한다.
            yield item


lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(list(flatten(lol)))  # yield 되는 item 들을 반환받아 리스트 형변환 한다.
# 결과: [1, 2, 3, 4, 5, 6, 7, 8, 9]
