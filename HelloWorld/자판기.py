class VendingMachine:
    # 함수를 이용
    def __init__(self):
        self.drink_menu = {'레몬' : 500, '물' : 600}
        self.money = 0

    def pay(self):
        money = int(input('돈을 넣어주세요 : '))
        self.money =  money

    def select(self):
        menu = input('메뉴를 선택해주세요 : ')
        cost = self.drink_menu[menu]
        return menu, cost

    def compare(self, menu, cost):
        if self.money >= cost:
            print('음료수를 받으세요.')
            self.money = self.money - cost
        else:
            print('돈이 부족합니다.')


    def question(self):
        print(self.money)
        answer = input('계속하시겠습니까?(네/아니요) : ')
        if answer == '네':
            return False
        elif answer == '아니요':
            return True


    def consequence(self):
        while True:
            self.pay()
            menu, cost = self.select()
            self.compare(menu, cost)
            answer = self.question()
            if answer:
                break

machine = VendingMachine()
machine.consequence()