class vending_machine:
    # 딕셔너리를 이용한 자판기 메뉴
    print('안녕하세요. drink입니다.')
    drink_menu = {'레몬' : 500, '물' : 600}
    # 함수를 이용
    def __init__(self, money):
        self.money = money
        return

    def pay(self, drink_menu):
        self.drink_menu = drink_menu
        self.peaple_money = peaple_money
        return peaple_money - drink_menu

    def get_drink_by_money(self, money):
        if money < self.drink_menu['레몬']:
            print('돈이 부족합니다')
        elif money < self.drink_menu['물']:
            print('1번만 골라주세요.')
        else :
            print('1번, 2번을 골라주세요')
    # while문을 이용
    while True:
        money = int(input('금액을 넣어주세요 : '))
    # if문을 이용
        if money < drink_menu['레몬']:
            print('돈이 부족합니다. 반환합니다')
        else :
            get_drink_by_money(money)
            menu = int(input('메뉴를 선택해주세요(1 : 레몬, 2 : 물) : '))
            if menu == 1:
                print('레몬이 선택되었습니다. 거스름돈은 입니다.')
            elif menu <= 2:
                print('물이 선택되었습니다. 거스름돈은 입니다.')
            else:
                print('취소되었습니다.')
            break

print("이용해 주셔서 감사합니다.")