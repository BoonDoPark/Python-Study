class Calculator:
    def __init__(self, a, b):
        # self.select = input().split(' ')
        self.a = a
        self.b = b

    def add(self):
        # a = 0
        # for i in self.select:
        #    a += int(i)
        return self.a + self.b

    def sub(self):
        # s = (int(self.select[0]) + int(self.select[0]))
        # for i in self.select:
        #    s -= int(i)
        return self.a - self.b

    def mul(self):
        # m = 1
        # for i in self.select:
        #    m *= int(i)
        return self.a * self.b

    def div(self):
        # d = int(self.select[0])*int(self.select[0])
        # for i in self.select:
        #    d /= int(i)
        return self.a / self.b

    def input(self):
        self.c = int(input())
        return self.c

    def add_process(self):
        add = self.add()
        input = self.input()
        self.d = add + input
        print(self.d)
        while True:
            input = self.input()
            if input == 0:
                break
            self.d += input
            return self.d

    def sub_process(self):
        sub = self.sub()
        input = self.input()
        self.d = sub - input
        print(self.d)
        while True:
            input = self.input()
            if input == 0:
                break
            self.d -= input
            return self.d

    def mul_process(self):
        mul = self.mul()
        input = self.input()
        self.d = mul * input
        print(self.d)
        while True:
            input = self.input()
            if input == 0:
                break
            self.d *= input
            return self.d

    def div_process(self):
        div = self.div()
        input = self.input()
        self.d = div / input
        print(self.d)
        while True:
            input = self.input()
            if input == 0:
                break
            self.d /= input
            return self.d