# 프로그래머의 날은 9월 12일, 9월 13일로 러시아에서는 휴일로 한다.
# 윤년이란, 한해에 365일이지만, 윤년은 366일로 2월에 하루가 추가된다.

year = int(input('년도 : '))

# 평년의 각 달마다 일수
days_per_month_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 윤년의 각 달마다 일수
days_per_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def calculate(days_per_month):
    anniversary = int(input('기념일 : '))
    for month, days in enumerate(days_per_month):
        if anniversary < days:
            print(f'{year}-{month+1}-{anniversary}')
            break
        anniversary -= days


if year <= 1917:
    # 윤년 (율리우스력 : 4년마다)
    if year % 4 == 0:
        calculate(days_per_month_leap)

    # 평년
    else:
        calculate(days_per_month_normal)

elif year == 1918:
    print('{}-09-26'.format(year))

elif year > 1918:
    # 그레고리력 : 4년마다 윤년, 400년마다 윤년이지만, 100년마다는 아닌 력.
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        calculate(days_per_month_leap)

    else:
        calculate(days_per_month_normal)

else:
    print('없는 날입니다.')
