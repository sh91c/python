"""
    객체와 클래스
"""
"""
    파이썬은 리스트, 딕셔너리 등을 포함한 다른 표준 데이터 타입을 생성하는 내장 클래스가 많이 있다.
    커스텀 객체(custom obj)를 생성해보기 위해 class 를 정의해보자.
    함수처럼 클래스명()으로 호출해, '클래스로부터 객체를 생성' 할 수 있다.
"""

# class Cat:
#     pass
#
#
# cat_1 = Cat()
# cat_2 = Cat()
# Cat()은 Cat 클래스로부터 개별 객체를 생성하고, 이런 객체를 cat_1과 cat_2에 할당한다.
# 그러나 Cat 클래스는 빈 클래스기 때문에 생성한 객체만 존재할 뿐, 할 수 있는게 없다!


"""
    속성(attribute)은 클래스나 객체 내부의 변수이다.
    객체나 클래스가 '생성 되는 동안' 또는 '생성 이후' 에 속성을 할당할 수 있다.
    속성(attr)을 이야기할 때, 일반적으로 객체속성을 의미함. 클래스 속성도 있다.
    아래는 객체에 여러 속성을 저장하는 과정임.
"""
# cat_1.age = 3
# cat_1.name = '야옹이_1'
# cat_1.namesis = cat_2
#
# print(cat_1.age)
# print(cat_1.name)
# print(cat_1.namesis)
#
# cat_1.namesis.name = '애옹이_2'
# print(cat_1.namesis.name)

"""
    메서드는 클래스 또는 객체의 함수.
"""

"""
    초기화. 객체를 생성할 때 속성을 할당하려면 객체 초기화 메서드 __init__() 을 사용.
    __init__(): 첫 번째 매개변수 이름은 self 여야하고, 매개변수는 개별 객체 자신을 참조하도록 지정함.(예약어는 아님.)
    아래는 하나 또는 하나 이상의 속성을 할당해보기.
    
    * __new__() 는 나중에 따로 할 것. (__init__() 보다 먼저 실행되는 메서드.)
    
    [__init__() 메서드]
    모든 클래스 정의에서 __init__() 메서드를 가질 필요가 없음.
    __init__ 메서드는 같은 클래스에서 생성된 다른 객체를 구분하기 위해 필요한 무언가를 수행한다.
    다른 언어에서 말하는 '생성자' 의 개념이 아님. 왜냐하면, 이미 __init__() 을 호출 전에 객체를 만들었기 때문이다.
    그래서, __init__() 은 초기화 메서드라고 함.
    
    [동작 순서]
    1. Cat 클래스의 정의를 찾는다
    2. 메모리에 새 객체를 초기화(생성)한다. == __init__() 메서드를 통해서.
    3. __init__() 메서드를 호출하며 새롭게 생성된 객체를 self 인자에 전달하고, 인수 ('야옹이_3') 를 name 인자에 전달한다.
    4. 해당 객체에 name 속성으로 전달받은 인자(값)을 저장한다.
    5. 새 객체를 반환한다.
    6. cat_3 변수에 이 객체를 연결한다.
"""

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#
# # 이제 Cat 클래스를 생성하면서, name 매개변수에 문자열을 전달해보자.
# cat_3 = Cat('야옹이_3')
# print(cat_3.name)

"""
    [상속(inherit)]
    기존 클래스에서 일부를 추가하거나 변경해 새 클래스를 생성.
    코드를 재사용(reuse)하는 방법.
    상속으로 기존 클래스를 복사할 필요없이 모든 코드를 사용할 수 있음.
    
    기존(부모) 클래스를 상속받아 필요한 것만 추가하거나, 변경해서 새 클래스를 정의할 수 있음.
    그리고 기존 클래스의 행동(behavior)을 재정의(override) 함.
    
    기존 클래스를 부를 때는 부모(parent) | 슈퍼(super) | 베이스(base) 클래스라고 부름.
    새 클래스를 부를 때는 자식(child) | 서브(sub) | 파생된(derived) 클래스라고 부름.
    객체 지향 프로그래밍(Object-Oriented Programming)에서 다르게 불릴 수 있음.
"""


class Car():
    def introduce(self):
        print("I'm a Car!")


class Bus(Car):
    # 메서드 오버라이드
    def introduce(self):
        print("I'm a Bus! Much like a Car, but more bus-ish.")

    # 메서드 추가
    def push(self):
        print('A little help here...?')


print(issubclass(Bus, Car))  # Bus 는 Car 의 서브 클래스인가? True

car = Car()
bus = Bus()

"""
    자식 클래스는 부모 클래스를 구체화(specialization) 한 것.
    OOP 용어로 Bus 는 Car 이다. (Bus is a Car.)
    bus 는 Bus 클래스의 인스턴스, Car 클래스가 할 수 있는 것을 상속 받았음.
    
    introduce 메서드를 오버라이드 했음.
    __init__() 메서드를 포함한 모든 메서드를 오버라이드 할 수 있음.
"""

car.introduce()
bus.introduce()
bus.push()


# 다른 예시
class Person:
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = f"Doctor {name}"


class JDPerson(Person):
    def __init__(self, name):
        self.name = f"{name} Esquire"


# person = Person('John')
# doctor = MDPerson('John')
# lawyer = JDPerson('John')

# print(person.name)
# print(doctor.name)
# print(lawyer.name)

# print(Person.mro())
# print(MDPerson.mro())
# print(JDPerson.mro())

"""
    자식 클래스에서 __init__() 메서드를 정의하면, 부모 클래스의 __init__() 을 재정의 하는 것이기 때문에,
    부모 클래스의 __init__() 메서드가 호출되지 않는다.
    
    [아래 클래스 동작순서]
    super().__init__(name) 에서의
        super() 메서드는 부모 Person 클래스의 정의를 얻음.
        __init__() 메서드는 Person.__init__() 메서드를 호출. self 인수를 슈퍼 클래스로 전달하는 역할.
        그렇기에 슈퍼 클래스에 선택적 인수를 제공하기만 하면 된다.
        이 경우 Person()에서 받을 인수는 name 이다.
        
    self.email = email 은 EmailPerson 클래스를 Person 클래스와 다르게 만들어줄 새로운 코드이다.
"""


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


bob = EmailPerson('Bob Oh', 'bob@babo.com')

# 해당 bob 객체의 name 과 email 속성에 접근 가능.
print(f"name: {bob.name} / email: {bob.email}")

"""
    위 코드에서,
    super() 메서드의 이점은, Person 클래스의 정의가 추후 바뀐다면
    EmailPerson 클래스의 속성과 메서드에 Person 클래스의 변경사항이 반영된다는 점.
"""