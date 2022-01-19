# 네임드 튜플
# namedtuple('이름', '스페이스로 구분된 필드 이름 문자열')
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill, "/", duck.tail)
# # 딕셔너리를 활용한 네임드 튜플
# parts = {'bill': 'wide orange', 'tail': 'long'}
# duck2 = Duck(**parts)
# print(duck2)
# # 네임드 튜플은 불변이다. 하지만 필드를 바꿔서 또 다른 네임드 튜플을 반환할 수 있다.
# duck3 = duck2._replace(tail='magnificent', bill='crushing')
# print(duck3)