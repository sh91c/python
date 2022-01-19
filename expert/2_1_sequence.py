# 내장 시퀀스 개요
# 컨테이너 시퀀스 : 서로 다른 자료형의 항목들을 담을 수 있는
# -> list, tuple, collections.deque 형
# 객체에 대한 참조를 담고 있음
# 객체는 어떠한 자료형도 될 수 있음

# 큔일 시퀀스 : 단 하나의 자료형만 담을 수 있는
# -> str, bytes, bytearray, memoryview, array.array 형
# 객체에 대한 참조 대신,
# 자신의 메모리 공간에
# 각 항목의 값을 직접 담는다.
# 따라서, 균일 시퀀스가 메모리를 더 적게 사용하지만
# 문자, 바이트, 숫자 등 기본적인 자료형만 저장할 수 있다.

# 가변성에 따른 분류
# 가변 시퀀스 : list, bytearray, array.array, collections.deque, memoryview 형
# 불변 시퀀스 : tuple, str, bytes 형