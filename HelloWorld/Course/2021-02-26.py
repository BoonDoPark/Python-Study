# 인덱스 슬라이싱
li = [10, 11, 21, 31, 14, 25, 36, 47]
print(li[0])
print(li[2])
print(li[0:3])
print(li[-1])
print(li[3:-1])
print(li[3:-2])
print(li[4:2:-1])

d = {'1': 'a', '2': 'b'}
keys = d.keys()
values = d.values()

# Comprehension
li = []
for i in range(100):
    li.append(i)
print(li)

li_2 = [i + 2 for i in range(100)]
print(li_2)

ts = (i + 2 for i in range(100))
for t in ts:
    print(t)


# 상속
class parent:
    def __init__(self):
        self.wealth = 100000000

    def love(self):
        print('사랑')


class child(parent):
    pass


p = parent()
p.love()
c = child()
c.love()
print(p.wealth)
print(c.wealth)


class animal:
    num = 10

    def __init__(self):
        self.name = '동물'

    def eat(self):
        print('먹기', self.name)

    def sleep(self):
        print('자기', self.name)

    def play(self):
        print('놀기', self.name)


class duck(animal):
    def __init__(self):
        self.name = '오리'

    # 자식 클래스가 부모 클래스의 메소드를 재정의하는 것을
    # 오버라이딩 이라고 한다.
    def play(self):
        print('놀기!!!!!', self.name)


d = duck()
d.eat()
d.sleep()
a = animal()
a.play()
d.play()


# 접근제한자
class Toy:
    def __init__(self):
        self.name = '장난감'
        self.price = 10000

    def _info(self):
        print('v1', self.name, self.price)

    def __info_v2(self):
        print('v2', self.name, self.price)

    def __info_v3__(self):
        print('v3', self.name, self.price)

    def beep(self):
        self._info()
        self.__info_v2()
        self.__info_v3__()
        print('삐빅')


class ToyCar(Toy):
    def run(self):
        self._info()
        # self.__info_v2()
        self.__info_v3__()
        print('슝슝')

toy = Toy()
toy._info()
toy.beep()

car = ToyCar()
car.run()
car.__info_v3__()

# 언더바(_)를 한번 쓰면 protected 접근제한자 : 자식클래스까지만 부모클래스의 멤버를 접근가능
# 언더바(_)를 두번 쓰면 private 접근제한자 : 부모클래스 자기 자신만 멤버를 접근가능 (자식조차 접근 불가)
# 근데 뒤에 언더바 두번을 쓰면 다시 public


class Accumulator:
    value = 10

    @staticmethod
    def add(x, y):
        return x + y, Accumulator.value

    @classmethod
    def plus_one(cls):
        return cls.value + 1, cls.add(cls.value, cls.value)


result, result_ = Accumulator.add(1, 2)
print(result, result_)
result2, result3 = Accumulator.plus_one()
print(result2, result3)

# @ : 데코라이터
# 정적메소드 : 객체를 생성하지 않아도 접근이 가능한 메소드
# @staticmethod : 참조할 것이 없을 때 써도 좋음
# @classmethod : 참조를 함


# 엘레베이터 만들기
# 두 개의 클래스가 필요하다. (ElevatorScheduler, Elevator)
# ElevatorScheduler의 역할 : 내가 버튼을 눌렀을때 어떤 엘레베이터가 동작할지 정해주는 역할
# 현재 시간이 오전일 때, 내 위치보다 먼곳의 엘레베이터를 동작
# 현재 시간이 오후일 때, 내 위치에 가까운 엘레베이터를 동작
# Elevator의 역할 : 엘레베이터 객체의 틀

