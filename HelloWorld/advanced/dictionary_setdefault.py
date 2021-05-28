# setdefault 를 알기 전, 각 키별로 기본값을 설정하는 방법
def set_default_value():
    d = dict()
    keys = [1, 2, 3, 4, 5]
    for k in keys:
        d[k] = list()
    print(d)
    print(d[6])


# setdefault 를 알고난 이후
def set_default_value_v2():
    d2 = dict()
    # 기본값 리턴
    res = d2.setdefault(1, list())
    print(d2)
    print(res)


# comprehension 응용
def set_default_value_v3():
    d3 = dict()
    keys = [1, 2, 3, 4, 5]
    [d3.setdefault(k, list()) for k in keys]
    print(d3)


# collections default dict
def init_default_dict():
    from collections import defaultdict
    d4 = defaultdict(int)
    print(d4['a'])
    d5 = defaultdict(list)
    print(d5)
    print(d5['b'])
