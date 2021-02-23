class vendingMachine:
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

Machine = vendingMachine()
Machine.consequence()
    # while문을 이용
    # while True:
    #     money = int(input('금액을 넣어주세요 : '))
    # # if문을 이용
    #     if money < drink_menu['레몬']:
    #         print('돈이 부족합니다. 반환합니다')
    #     else :
    #         menu = int(input('메뉴를 선택해주세요(1 : 레몬, 2 : 물) : '))
    #         if menu == 1:
    #             print('레몬이 선택되었습니다. 거스름돈은 입니다.')
    #         elif menu <= 2:
    #             print('물이 선택되었습니다. 거스름돈은 입니다.')
    #         else:
    #             print('취소되었습니다.')
    #         break

print("이용해 주셔서 감사합니다.")