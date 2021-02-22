class drinks:
    w = {'레몬' : 500, '물' : 600}

    def __init__(self, money):
        self.money = money
        return

    def get_drink_by_name(self, money):
        if money < self.w['레몬']:
            print('돈이 부족합니다')
        elif money < self.w['물']:
            print('레쓰비를 고를 수 있습니다.')
        else :
            print('둘 다 고를 수 있습니다')

while True:
     japangi = drinks(0)
     money = int(input('금액을 넣어주세요 : '))
     if money < japangi.w['레몬']:
            print('돈이 부족합니다. 반환합니다')
     else :
        japangi.get_drink_by_name(money)
        menu = int(input('메뉴를 선택해주세요(1 : 레몬, 2 : 물) : '))
        if menu == 1:
            print('레몬이 선택되었습니다. 거스름돈은 ')
        elif menu == 2:
            print('물이 선택되었습니다. 거스름돈은 ')
        else:
            print('취소되었습니다.')
            break

print("이용해 주셔서 감사합니다.")