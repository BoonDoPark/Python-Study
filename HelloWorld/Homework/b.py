# 프로그래머의 날은 9월 12일, 9월 13일로 러시아에서는 휴일로 한다.
# 윤년이란, 한해에 365일이지만, 윤년은 366일로 2월에 하루가 추가된다.

year = int(input('년도 : '))

# 평년의 각 달마다 일수
day1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 윤년의 각 달마다 일수
day2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year <= 1917:
    # 율리우스력 : 4년마다 윤년.
    if year % 4 == 0:
        num = 0
        d = int(input('기념일 : '))
        # 리스트안에서 요소를 다 합해야 하기 때문에, for문으로 리스트의 합을 구했다.
        for i in day2:
            num = num + i
            for j in range(len(day2)):
                a = j + 1
            # 원래는 256에서 243일을 빼지만, 윤년에는 2월에 1일이 추가되기 때문에,
            # 프로그래머의 날은 9월 12일로 된다.
            if num < d:
                day = d - num
        print('{}-{}-{}'.format(year, a, day))
    else:
        num = 0
        d = int(input('기념일 : '))
        for i2 in day1:
            num = num + i2
            if num < d:
                day = d - num
        print('{}-09-{}'.format(year, day))

elif year == 1918:
    print('{}-09-26'.format(year))

elif year > 1918:
    # 그레고리력 : 4년마다 윤년, 400년마다 윤년이지만, 100년마다는 아닌 력.
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        num = 0
        d = int(input('기념일 : '))
        for i in day2:
            num = num + i
            if num < d:
                day = d - num
        print('{}-09-{}'.format(year, day))

    else:
        num = 0
        d = int(input('기념일 : '))
        for i2 in day1:
            num = num + i2
            if num < d:
                day = d - num
        print('{}-09-{}'.format(year, day))
else:
    print('없는 날입니다.')