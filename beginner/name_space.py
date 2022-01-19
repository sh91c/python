"""
    이름(name)은 사용되는 위치에 따라 다른 것을 참조할 수 있다.
    파이썬에는 다양한 네임스페이스(namespace)가 있다.
    네임스페이스에는 특정 이름이 유일하고, 다른 네임스페이스에서
"""
animal = 'fruitbat'


def print_grobal():
    print('inside print_grobal:', animal)


print('at the top level:', animal)
print_grobal()