import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
# print(beer_card)

deck = FrenchDeck()
# print(len(deck))
# print(deck[0])  # FrenchDeck의 __len__()에서 제공
# print(deck[-1])  # FrenchDeck의 __getitem__()에서 제공
#
# print(choice(deck))
# print(choice(deck))
# print(choice(deck))


# 특별 메서드를 통해 파이썬 데이터 모델을 사용할 때의 두 가지 장점
# 1. 사용자가 표준 연산을 수행하기 위해 클래스 자체에서 구현한
# 임의 메서드명을 암기할 필요가 없다.
# 2. 파이썬 표준 라이브러리에서 제공하는 풍부한 기능을 별도로
# 구현할 필요없이 바로 사용할 수 있다.

# __getitem__() 메서드는 self._cards의 [] 연산자에 작업을 위임하므로
# deck 객체는 슬라이싱도 자동으로 지원한다.

# print(deck[:3])
# print(deck[12::13])

# __getitem__() 특별 메서드를 구현함으로써 deck을 반복할 수도 있다.
# for card in deck:  # doctest: +ELLIPSIS
#     print(card)

# 뒤에서부터 반복할 수도 있다.
# for card in reversed(deck):
#     print(card)

# 정렬
suit_values = dict(spades=3,
                   hearts=2,
                   diamonds=1,
                   clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)

# __len__()과 __getitem__() 특별 메서드를 구현함으로써
# 표준 파이썬 시퀀스처럼 작동하게 됌
# 반복 및 슬라이싱 등의 핵심 언어 기능 및
# 표준 라이브러리를 사용할 수 있음

