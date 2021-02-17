class buri:
    def __init__(self, first, second):
        print('this is juicy')
        self.first = first
        self.second = second

    def add(self, a, b):
        return a+b

    def sub(self, c, b):
        return c-b

    def mul(self, a, b):
        return a*b

h = buri(1, 10000)
print(h, type(h))
q = h.mul(1, 1000)
w = h.sub(5000, 1000)
print(q, w)

j = {'주스':1000}
print(j, type(j))