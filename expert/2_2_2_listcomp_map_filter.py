# 예제: 지능형 리스트와 맵/필터 구성으로 만든 동일 리스트

# symbols = '가나다라마'
# beyond_ascii = [ord(s) for s in symbols]
# print(beyond_ascii)
#
# beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
# print(beyond_ascii)

# map()/filter()를 조합한 방법이 리스트 컴프리헨션보다 빠르다고 생각하고 있었지만(저자)
# 알렉스 마르텔리의 지적에 따라 적어도 위의 예제는 그렇지 않다는 것을 알게되었음(사견)
# 5장에서 맵/필터 조합을 자세히 다룸

# 데카르트 곱 : 두 개 이상의 리스트에 있는 모든 항목을 이용해서 만든 튜플로 구성된 리스트
# 지능형 리스트(comp)는 두 개 이상의 반복 가능한 자료형의
# 데카르트 곱을 나타내는 일련의 리스트를 만들 수 있다.
# 데카르트 곱 안에 들어 있는 각 항목은
# 입력으로 받은 반복 가능한 데이터의
# 각 요소에서 만들어진 튜플로 구성된다.
# 생성된 리스트의 길이는 입력으로 받은 반복 가능한 데이터의 길이와 동일하다

# 두 가지 색상과 세 가지 크기의 티셔츠 리스트를 만드는 경우
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# tshirts = [(color, size)for color in colors for size in sizes]
# print(tshirts)
# 지능형 리스트는 단지 리스트를 만들 뿐이다.
# 다른 종류의 시퀀스를 채우려면 제너레이터 표현식을 사용해야한다.

# 제너레이터 표현식
# 튜플, 배열 등의 시퀀스형을 초기화하려면 지능형 리스트를 사용할 수도 있지만,
# 다른 생성자에 전달할 리스트를 통째로 만들지 않고
# 반복자 프로토콜(iterator protocol)을 이용해서
# 항목을 하나씩 생성하는 제너레이터 표현식은 메모리를 더 적게 사용한다.
# 제너레이터 표현식은 지능형 리스트와 동일한 구문을 사용하지만, 대괄호 대신 괄호를 사용한다.

# 제너레이터 표현식에서 튜플과 배열 초기화하기
# symbols = "가나다라마"
# result = tuple(ord(symbol) for symbol in symbols)
# print(result)
# # print(result)
#
# import array
#
# result = array.array('I', (ord(symbol) for symbol in symbols))
# print(result)

# 제너레이터 표현식에서의 데카르트 곱
# 한 번에 하나의 항목을 생성하며, 리스트는 만들지 않는다.(메모리 사용 X)
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c}, {s}' for c in colors for s in sizes):
    print(tshirt)