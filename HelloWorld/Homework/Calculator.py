class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        a = self.first + self.second
        return a

    def sub(self):
        s = self.first - self.second
        return s

    def mul(self):
        m = self.first * self.second
        return m

    def div(self):
        d = self.first / self.second
        return d


c = Calculator(100, 50)
a = c.add()
s = c.sub()
m = c.mul()
d = c.div()

print(a)
print(s)
print(m)
print(d)
