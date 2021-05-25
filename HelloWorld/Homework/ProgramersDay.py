# 프로그래머의 날은 9월 12일, 9월 13일로 러시아에서는 휴일로 한다.
# 윤년이란, 한해에 365일이지만, 윤년은 366일로 2월에 하루가 추가된다.

year = int(input('년도 : '))

# 평년의 각 달마다 일수
day_month_nomal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 윤년의 각 달마다 일수
day_month_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year <= 1917:
    # 율리우스력 : 4년마다 윤년.
    if year % 4 == 0:
        day = 0
        day_cal = int(input('기념일 : '))
        # 리스트안에서 요소를 다 합해야 하기 때문에, for문으로 리스트의 합을 구했다.
        for days in day_month_leap_year:
            day = day + days
            # 원래는 256에서 243일을 빼지만, 윤년에는 2월에 1일이 추가되기 때문에,
            # 프로그래머의 날은 9월 12일로 된다.
            if day < day_cal:
                special_day = day_cal - day
        print('{}-09-{}'.format(year, special_day))
    else:
        day = 0
        day_cal = int(input('기념일 : '))
        for days in day_month_nomal_year:
            day = day + days
            if day < day_cal:
                special_day = day_cal - day
        print('{}-09-{}'.format(year, special_day))

elif year == 1918:
    print('{}-09-26'.format(year))

elif year > 1918:
    # 그레고리력 : 4년마다 윤년, 400년마다 윤년이지만, 100년마다는 아닌 력.
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        day = 0
        day_cal = int(input('기념일 : '))
        for days in day_month_leap_year:
            day = day + days
            if day < day_cal:
                special_day = day_cal - day
        print('{}-09-{}'.format(year, special_day))

    else:
        day = 0
        day_cal = int(input('기념일 : '))
        for days in day_month_nomal_year:
            day = day + days
            if day < day_cal:
                special_day = day_cal - day
        print('{}-09-{}'.format(year, special_day))
else:
    print('없는 날입니다.')