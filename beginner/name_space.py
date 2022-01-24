"""
    요약: 지역변수, 전역변수를 로컬 네임스페이스, 글로벌 네임스페이스라고 부르는듯.
    네임스페이스에 접근하기 위해 두 가지 함수를 제공
    locals() 함수는 로컬 네임스페이스 내용을 딕셔너리로 반환
    globals() 함수는 글로벌 네임스페이스 내용을 딕셔너리로 반환
"""
animal = 'fruitbat'


def change_local():
    animal = 'wombat'  # 지역 변수
    print('locals():', locals())


print(animal)  # fruitbat
change_local()  # locals(): {'animal': 'wombat'}
print('globals():', globals()['animal'])  # globals(): fruitbat

# 아래 주석은 globals() 전체 값
# globals(): {'__name__': '__main__', '__doc__': '\n    요약: 지역변수, 전역변수를 로컬 네임스페이스, 글로벌 네임스페이스라고 부르는듯.\n
# 네임스페이스에 접근하기 위해 두 가지 함수를 제공\n    locals() 함수는 로컬 네임스페이스 내용을 딕셔너리로 반환\n
# globals() 함수는 글로벌 네임스페이스 내용을 딕셔너리로 반환\n', '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000162AEBD0608>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:\\Users\\choi\\Documents\\GitHub\\mainPythonProject\\beginner\\name_space.py',
# '__cached__': None, 'animal': 'fruitbat', 'change_local': <function change_local at 0x00000162AEC25E58>}

