class Calculator:
    def __init__(self, first, second):
        print('hello, i\'m calculator')
        self.first = first
        self.second = second

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def mul_by_init(self):
        return self.first * self.second

def add(a, b):
    return a + b


def init_list_by_num(num):
    lis = list()
    for n in range(num):
        lis.append(n)
    return lis


if __name__ == '__main__':
    # 조건문 (if ~ else / elif문)
    if 10 == 10:
        print('참')
    else:
        print('거짓')

    if 10 > 20:
        print('a')
    elif 10 > 8:
        print('b')

    # 변수
    a = 10
    print(a, type(a))
    b = '10'
    print(b, type(b))

    # 변수 타입
    # 정수, 실수, 문자열, boolean
    c = 3.14
    print(c, type(c))
    d = 10 == 10
    e = 10 != 10
    print(d, type(d))
    print(e, type(e))

    # 자료형 - 값을 여러개를 보관할 수 있는 애들
    # 리스트([]), 튜플(()), 세트(set) - 중복을 허용하지 않음, 딕셔너리({})
    # 리스트
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(l1, type(l1))

    l2 = list()
    l2.append(1)
    l2.append(2)
    pop_ = l2.pop(0)
    print(pop_)
    l2.append(pop_)
    print(l2, type(l2))
    # 인덱스 - 몇번째인지를 의미해
    print(l1[0])
    print(l1[1])

    # 딕셔너리
    # 키와 밸류의 쌍
    d1 = {'k1': 'v1', 'k2': 'v2'}
    print(d1, type(d1))
    print(d1['k2'])

    d2 = dict()
    d2['k3'] = 'v3'
    d2['k4'] = 'v4'
    print(d2, type(d2))
    print(d2.keys())
    print(d2.values())
    print(d2.items())

    # 반복문 (for문, while문)
    # Iterable한 객체를 순회한다.
    l3 = list()
    alphas = 'abcdefghijklmnop'
    for alpha in alphas:
        l3.append(alpha)
        print(l3)

    for key in d2.keys():
        print(d2[key])

    for value in d2.values():
        print(value)

    for key, value in d2.items():
        print(key, value)

    # enumerate
    for index, value in enumerate(l1):
        if index % 2 == 0:
            print(index, value)

    # 함수 (method, function)
    plus = add(10, 20)
    print(plus)

    lis_10 = init_list_by_num(10)
    lis_100 = init_list_by_num(100)
    for i in range(100):
        print(init_list_by_num(i))

    # 클래스
    c = Calculator(10, 200)
    print(c, type(c))
    p = c.add(1, 2)
    m = c.sub(2, 1)
    g = c.mul(2, 3)
    n = c.div(6, 3)
    print(p, m, g, n)
    print(c.mul_by_init())