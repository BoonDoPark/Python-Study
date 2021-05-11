class Calculator:
    first = int(input('숫자 : '))
    second = int(input('숫자 : '))

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

c = Calculator()
p = c.add()
s = c.sub()
m = c.mul()
d = c.div()
print(p)
print(s)
print(m)
print(d)

