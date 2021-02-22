class drink:
    x = '레쓰비', 500
    y = '물', 600
    def __init__(self, money):
        self.money = money
        return

    def get_drink_by_name(self, money):
        if money < self.x:
            print('돈이 부족합니다')
        elif money < self.y:
            print('레쓰비를 고를 수 있습니다.')
        else :
            print('둘 다 고를 수 있습니다')
    while 1:
        japangi = drink
        money = int(input('금액을 넣어주세요 : '))
        if money < japangi.x:
            print('돈이 부족합니다. 반환합니다')
        else :
            menu = int(input('메뉴를 선택해주세요(1.레쓰비, 2.물 : '))
        break