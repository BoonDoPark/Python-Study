class VendingMachine:
    # 함수를 이용
    def __init__(self):
        self.drink_menu = {1: ('레몬', 500), 2: ('물', 600), 3: ('환타', 700), 4: ('커피', 1000)}
        # self.drink_menu = {'레몬': 500, '물': 600, '환타': 700, '커피': 1000}
        self.money = 0

    def input(self):
        money = int(input('돈을 넣어주세요 : '))
        self.money = self.money + money

    def show_menu(self):
        menus = self.drink_menu.keys()
        for menu in menus:
            menu_name, cost = self.drink_menu[menu]
            print('{0}. {1} {2}'.format(str(menu), menu_name, cost))

    def select(self):
        self.show_menu()
        _idx = int(input('메뉴를 선택해주세요. : '))
        if _idx not in self.drink_menu.keys():
            print('없는 메뉴입니다.')
            return None, None
        menu_name, cost = self.drink_menu[_idx]
        return menu_name, cost

    def compare(self, menu, cost):
        if self.money >= cost:
            print('{0}를 받으세요.'.format(menu))
            self.money = self.money - cost
        else:
            print('돈이 부족합니다.')

    def question(self):
        print(self.money)
        answer = input('계속하시겠습니까?(네/아니요) : ')
        if answer == '네':
            return True
        elif answer == '아니요':
            return False

    def process(self):
        while True:
            self.input()
            menu, cost = self.select()
            if not menu or not cost:
                return
            # self.compare(menu, cost)
            answer = self.question()
            if answer:
                break


machine = VendingMachine()
machine.process()
