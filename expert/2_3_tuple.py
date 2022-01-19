# 튜플은 단순한 불변 리스트가 아니다.
# 불변 리스트로 사용할 수도 있지만,
# 필드명이 없는 레코드로 사용할 수도 있다.

# 레코드로서의 튜플
# 튜플은 레코드를 담고 있다.
# 각 항목은 레코드의 필드 하나를 의미
# 항목의 위치가 의미를 결정

# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)
#     # 튜플의 항목의 위치가 항목의 의미를 나타내는데
#     # 정렬을 한다면 정보가 파괴된다는 점에 주의할 것
#
# for country, _ in traveler_ids:
#     print(country)

# 내포된 튜플 언패킹
# metro_areas = [
#     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#     ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
# ]
#
# print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# fmt = '{:15} | {:9.4f} | {:9.4f}'
# for name, cc, pop, (latitude, longitude) in metro_areas:
#     if longitude <= 0:
#         print(fmt.format(name, latitude, longitude))


# 네임드 튜플
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo.population)
# print(tokyo.coordinates)
# print(tokyo[1])

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
for k, v in delhi._asdict().items():
    print(k, ':', v)