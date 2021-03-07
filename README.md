# Python
Learning Python.  
※ 모듈 사용 (copy, datetime, pandas, os, openpyxl, pickle, json, Selenium ..)

## Course

### 클래스(class)

클래스란 **객체의 타입**을 정의한 형태이며, **멤버**(필드, 함수)를 가진다. 클래스는 **응집도(cohension)가 높고 결합도(coupling)이 낮도록** 설계해야한다.
~~클래스란 코딩을 시작하기 전에 틀을 짜는 것을 의미한다. 클래스의 명칭에 따라 코딩의 주제가 바뀌기 때문에 클래스명에 신경을 많이 써야한다.~~
```
class 클래스명:
  ...
```

### 생성자 (constructor)
생성자는 클래스를 통해 객체(instance)를 생성하는 역할을 한다. 예를들어..  
```
class Person:
  def __init__(self):
    ...
    
person = Person()
```
클래스명()을 호출하게되면 실제로 호출되는 것은 클래스의 매직메소드 중 하나인 __init__() 메소드가 호출된다. 그리고 Person()은 Person 타입의 객체가 되어 person이라는 변수에 할당(assign)된다.

### while문, break문

반복해서 사용할 때 while문이 필요하다. 예를 들어, 음악을 100번 재생하고 싶다면,
```python
song_play = 0
while song_play < 100:
  song_play = song_play + 1
  print('노래를 %d번 재생합니다' %song)
 ```
 
음악을 100번 재생할 때 까지 계속 반복된다. 만약에 음악재생을 50번째에서 멈추고 싶다면
 ```python
song_play = 0
while song_play < 100:
  song_play = song_play + 1
  print('노래를 %d번 재생합니다' %song_play)
  if song_play == 50:
    print('재생을 멈춥니다.')
    break
 ```
위와 같은 break문으로 50번째에서 음악재생을 멈출 수 있다.

### 리스트(list)

리스트는 영어 뜻 그대로 목록이고, **순서**가 있는 **수정가능한** 객체이다. 리스트는 대괄호([]) 표현을 한다.

```python
l1 = [1, 2, 2, 3, 4, 5]
l1.count(2)  # 1
l1.append(8)  # [1, 2, 2, 3, 4, 5, 8]
l1.insert(4, 2)  # [1, 2, 3, 4, 2, 5, 8]
l1.sort()  # [1, 2, 2, 3, 4, 5, 8]
l1.count(8)  # 1

l2 = [1, 2, 3, 4]
l2.reverse()  # [4, 3, 2, 1]
l2.remove(2)  # [4, 3, 1]

l2.pop(0)  # 4
print(l2)  # [3, 1]

l2.extend([2, 9])
print(l2)  # [3, 1, 2, 9]
```

위에서 보면 append는 l1이라는 리스트에 8을 추가하겠다는 뜻이다. count는 l1의 리스트에 중복된 2라는 숫자의 갯수를 알 수 있다. insert는 l1의 4번째 열(index)에 2를 삽입하겠다는 뜻이다. sort는 l1의 리스트를 오름차순 정돈해준다. reverse는 l2의 리스트의 목록을 거꾸로 전환해준다. remove는 인자(argument)로 넘긴 요소를 제거해준다. 그래서, l2리스트에 2를 제거해주는 것을 확인할 수 있다. pop은 열의 0번째를 삭제해주었다. extend는 말그대로 확장이라는 뜻이다. l2리스트에 2, 9라는 숫자를 리스트에 추가해주었다.

### 튜플(tuple)

튜플(tuple)은 ()을 사용한다. 또, 리스트(list)와 거의 비슷하지만 몇가지 다른점이 있다.

```python
t1 = 1, 2
print(t1)

t2 = (10)
print(type(t2))

t2 = (10,)
print(type(t2))
```

위처럼 첫번째는 **괄호를 생략해도 괜찮다.** 두번째로 **t2의 type은 숫자(int)로 나온다. 하지만 10에 comma를 추가하면 숫자(int)타입에서 튜플(tuple)타입으로 바뀐다.** 하나의 요소만 있는 튜플은 comma를 사용해야 튜플로 사용이 된다. 리스트(ilst)는 생성, 삭제, 추가가 가능하지만, 튜플(tuple)은 한번 생성되면 바꿀수 없다. 또한, 튜플(tuple)은

```python
t1 = 11, 25, 36, 27, 59, 30
print(t1[3])  # 27
```

위와 같이 순서가 있기 때문에, 인덱싱 가능하다.

### 딕셔너리(dict)

딕셔너리란 사전이란 뜻이고, **key와 value를 한쌍**으로 갖는다.

```python
animal = {'육식동물': '호랑이', '초식동물': '기린'}
print(animal['육식동물'])
animal = {'육식동물': '호랑이', '육식동물': '사자'}
```
위와 같이 육식동물을 key, 호랑이를 value로 육식동물을 찾으면 호랑이가 나온다. key가 동일하고 value가 다를 땐 뒤에는 있는 사자만 나오니 주의해야 한다.
딕셔너리의 key와 value의 수가 많이 있다고 할때, key만 보고싶으면 dict클래스의 keys() 메소드를 호출하여 key를 찾을 수 있다. 

```python
animal = {'육식동물':'호랑이', '초식동물':'기린'}
animal.keys()
animal.values()
print(animal.values())
print(animal.keys())
```
위와 같이 keys인 이유는 key가 단수가 아니라 복수이기 때문이다. 마찬가지로 value를 찾을때도 이와 같다. 어떤 key가 그 안에 있는지 확인하고 싶을때는 in을 사용하면 된다.  

```python
animal = {'육식동물':'호랑이', '초식동물':'기린'}
print('육식동물' in animal)
```
위와 같이 코드를 입력하면 True가 나와 key에 육식동물이 있다는 걸 증명한다.  

```
animal.items()
dict_items([('육식동물', '호랑이'), ('초식동물', '기린')])
```
dict클래스의 items() 메소드를 호출하면 키와 값의 쌍(튜플 형태)의 목록(리스트)을 얻을 수 있다.

### 집합(set)

집합(set)은 집합에 관련된 것을 편리하게 처리하기 위한 것이다.

```python
s1 = set('i saw miracle')
print(s1)
```

출력하면 {'i', 'r', 's', 'l', 'e', 'c', 'w', 'm', 'a', ' '}이 출력된다. 출려된 결과값을 보면 집합(set)는 **요소가 중복하지 않는다.** 또, **요소의 순서가 정해져 있지 않다**는 걸 알 수 있다. 그래서, 인덱싱으로 값을 얻을 수 없다. 값을 얻고 싶다면 리스트로 바꿔주어야한다. 에를들어,

```python
s1 = set([1, 2, 3, 4, 5])
print(s1)
l1 = list(s1)
print(l1)
print(l1[1])
```

위처럼 리스트로 변환을 한 후에 인덱싱을 사용할 수 있다.

### for문

다른 언어에서는 for문이 여러가지 있지만 파이썬에선 for in만 쓸 수 있다. 예를 들어 키가 다 같은 사람들이 있다는 가정하에
```python
weight = [87, 71, 89, 84, 71]
number = 0
for weight in weight:
    number = number + 1
    if weight >= 85:
        print('%d번은 비만입니다.' %number)
    else :
        print('%d번은 정상체중입니다.' %number)
```
위와 같이 비만인 사람과 정상체중인 사람을 출력해준다. for in문에는 range, enumerate이 있다. range는 숫자함수를 자동으로 만들어주는 역활이다. 예를들어

```python
add = 00
for i in range(10):
    add = add + i
    print(add)
```
위와 같이 표현할수 있다. enumerate은 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있다. 예를들어

```python
number = [1, 2, 3, 4, 5]
for idx, number in enumerate(number):
    print('{}번째, {}'.format(idx+1, number))
```
위와 같이 표현해서 몇번째에 어느 숫자가 있는지를 알 수 있다.  

### if문
조건을 판단한 후 그 상황에 맞게 처리해야 할 경우가 생긴다. 이때 if문을 통하여 상황을 수행할 수 있다.

```python
money = 10000
icecream = 6000
if money > icecream:
    print('아이스크림을 살 수 있습니다.')
else:
    print('아이스크림을 살 수 없습니다.')
```
위와 같이 money는 icecream보다 크기 때문에 '아이스크림을 살 수 있습니다'라고 출력이 된다. 그리고 if문엔 elif가 있다. elif는 else+if를 합친 단어이다.  

```python
money = 10000
icecream = 6000
if money > icecream:
    print('아이스크림을 살 수 있습니다')
else:
  ifmoney == icecream:
      print('아이스크림을 살 수 있습니다')
  else:
      print('아이스크림를 살 수 없습니다')
```

위와 같이 표현했으나 이러면 너무 코드가 조잡해지기 때문에,
```python
money = 10000
icecream = 6000
if money > icecream:
    print('아이스크림을 살 수 있습니다')
elif money == icecream:
    print('아이스크림을 살 수 있습니다')
else:
    print('아이스크림를 살 수 없습니다')
```
위와 같이 elif로 줄여 코드를 깔끔하게 해줄 수 있다.

### 함수(function)

함수란, **입력값**(input, argument)을 가지고 어떤 일을 수행한 다음에 그 결과물을 내어놓는 것이다. 프로그래밍 코드를 작성하다보면 반복되는 코드를 줄여주기 위해 특정 코드를 함수안에 정의하고, 그 코드를 함수명칭을 호출함으로써 코드를 실행하게 해준다.(**재사용성** 및 **가독성**증가) 또, 함수를 사용하는 또 다른 이유는 자신이 만든 프로그램을 함수화하면 프로그램 흐름을 일목요연하게 볼 수 있기 때문이다. 마치 공장에서 원재료가 여러 공정을 거쳐 하나의 상품이 되는 것처럼 프로그램에서도 입력한 값이 여러 함수를 거치면서 원하는 결괏값을 내는 것을 볼 수 있다. 이렇게 되면 프로그램 흐름도 잘 파악할 수 있고 오류가 어디에서 나는지도 바로 알아차릴 수 있다. 함수의 구조를 예를 들면,
```python
def mul(a, b): 
    if a < b:
        print('식은 성립하지 않는다.')
    else:
        print('식은 성립한다.')
    return a*b
    
number = mul(2, 20)
print(number)
```
위와 같이 곱하기(multiplication)의 함수를 사용해서 출력했다.

### 인덱스 슬라이싱

인덱스 슬라이싱의 슬라이싱은 '잘라낸다'라는 뜻이다. 인덱스 슬라이싱은 지정된 시작 인덱스부터 마지막 인덱스를 잘라서 가져온다. 다만, 한가지 조심해야 할 것은 마지막 인덱스는 가져오려는 인덱스에 포함되지 않기 때문에 항상 생각한 인덱스보다 1을 더 지정해야 한다. 예를들어,

```python
l1 = [13, 22, 54, 36, 58, 29, 17, 6, 25]
print(l1[2:7])
print(l1[1:-1])
print(l1[1:-1:3])
print(l1[:7])
print(l1[6:])
print(l1[::-3])
```

위의 l1[2:7]은 2번째부터 7번째전의 요소를 가져온다. **인덱스는 1부터가 아니라 0부터 시작한다.** l1[1 : -1]에서 **-n은 뒤에서 n 번째 요소**를 뜻한다. 1:-1이니 -2에 있는 요소 즉 13, 25를 제외한 모든 요소를 가져온다. l1[1 : -1:3]은 인덱스의 증가폭을 사용한다. [1: -1:3]는 1에서 -1까지 증가폭 3을 지정한 요소만 가져온다. l1[:7]은 인덱스의 7부터 끝 인덱스까지 빼고 가져온다. l1[6:]은 첫 인덱스부터 6까지 빼고 가져온다. l1[:: -3]에서 colon이 두개 들어가고 그 다음 숫자가 들어오면 숫자만큼의 증가폭을 가져온다. -3은 끝 인덱스부터 첫 인덱스까지 증가폭3만큼인 요소를 가져온다는 뜻이다. 또, range에서도 인덱스 슬라이싱이 사용할 수 있다.

```python
l2= range(10)
print(l2)
print(l2[2:9])
print(list(l2[2:9]))
```

위와 같이 range도 인덱스 슬라이싱이 가능하다. range는 요소가 모두 포함되지않고 범위만을 알려주기 때문에, list로 변환해서 요소를 생성시켜 확인한다.

### 표현식(Comprehension)

표현식(comprehension)은 for in반복문이나 if문을 사용하여 컬렉션 내부의 원소들을 구성시킬 수 있습니다. 표현식(comprehension)에는 리스트, 딕셔너리를 사용해서 만들 수 있다. 예를들어,
+ 컬렉션 : 파이썬에서 기본적인 데이터의 집합타입이 존재한다. 그 중에서 컬렌션의 종류는 리스트(list), 딕셔너리(dictanary), 튜플(tuple), 셋(set)이 있다.

```python
l1 = [13, 22, 54, 36, 58, 29, 17, 6, 25]
for i, v in enumerate(l1):
    print(i, v)

l1 = [i for i in enumerate(l1)]
print(l1)
```

위와 같이 l1의 for문을 이용하여 출력하고 있다. 하지만 표현식을 이용하여 for문을 간결하게 했다. 복잡한 코드를 간결하게 해준다. 그리고 딕셔너리를 사용해서 만들 수 있다. 예를들어,

```python
country_capital = {'대한민국': '서울', '영국': '런던', '미국': '워싱턴', '일본': '도쿄'}
country_capital = {capital: country for country, capital in country_capital.items()}
print(country_capital)
```

위와 같이 딕셔너리를 사용하여 표현식을 만들어 낼 수 있다.

### 상속(inheritance)

상속(inheritance)이란 사전 뜻은 '어떤 것을 물려 받는다.'이다. 사전의 뜻처럼 부모클래스의 멤버를 자식클래스로 물려주는 것을 뜻한다. 예를들어,

```python
class DrinkMenu:
    def __init__(self):
        self.name = '음료수'

    def price(self):
        print(1300, self.name)

class Cola(DrinkMenu):
    def __init__(self):
        self.name = '콜라'
    
    # 부모클래스의 price() 메소드를 자식클래스인 Cola에서 재정의 (오버라이딩)
    def price(self):
        print(1000, self.name)
        print('override')


DM = DrinkMenu()
DM.price()

c = Cola()
c.price()
```

위처럼 부모클래스인 DrinkMenu의 속성과 메소드를 자식클래스 cola가 사용할 수 있는 것을 확인할 수 있다. 그리고 부모클래스의 속성과 메소드를 상속를 받고, 자식클래스에서 재정리 할 수 있다. 그것을 **오버라이딩(overriding)** 이라고 한다. 그리고, 파이썬은 다중상속도 가능하다. 에를 들어,

```python
class DrinkMenu:
    def __init__(self):
        self.name = '음료수'

    def price(self):
        print(1300, self.name)

class IsCarbonate:
    def __init__(self):
        self.is_carbonate = True

class Cola(DrinkMenu, IsCarbonate):
    def __init__(self):
        self.name = '콜라'
        
class OrangeJuice(DrinkMenu, IsCarbonate):
    def __init__(self):
        self.name = '오렌지주스'
        self.is_carbonate = False

DM = DrinkMenu()
DM.price()

c = Cola()
c.price()

o = OrangeJuice()
o.price()
```

위처럼 부모클래스에 자식클래스가 두개여도 되고 부모클래스가 2개여도 상관없다. 다중상속엔 개수는 제한이 없다.

### 접근제한자(Access Modifier)

접근제한자(Access Modifier)는 말 그대로 다른 사람이 나의 가상환경에 접근을 못하게 하고싶거나 제한하고 싶을 때 사용한다. 예를들어,

```python
class Drink:
    def __init__(self):
        self.menu = '음료수'
        self.price = 1200

    def _info(self):
        print(self.menu, self.price)

    def __info__(self):
        print(self.menu, self.price)

    def __info(self):
        print(self.menu, self.price)

class Cola(Drink):
    def drink(self):
        self._info()
        # self.__info()
        self.__info__()
        print('콜라로 부탁해요')


drink = Drink()
drink._info()
# drink.__info()

c = Cola()
c.__info__()
c.drink()
```

위와 같이, 언더바(_)를 한번 쓰면 protected 접근제한자로, class Drink의 내부에서만 사용할 수 있습니다. 하지만,  자식클래스는 부모클래스의 언더바(_)를 한번 쓴 함수에 접근할 수 있다. 언더바(_)를 두번 쓰면  private 접근제한자로, 외부와 자식클래스까지 접근이 할 수 없다. 만약, class Drink의 언더바(_)를 두번 쓴 함수를 출력하면 AttributeError가 뜨기 때문에, 주의해야 한다. 그러나, 뒤에 언더바(_)를 두번쓰면 AttributeError에서 public이 된다.

### 정적메소드 (@staticmethod, @classmethod)

지금까지 클래스(class)가 메소드를 사용할때 객체를 생성해서 호출해왔다. 하지만, 정적메소드는 객체를 생성하지 않아도 접근이 가능한 메소드이다. 정적메소드는 두가지가 있다.**@staticmethod, @classmethod**이다. 정적메소드는 self를 받지 않으므로 인스턴스가 필요없을때 사용한다. 예를들어,
+ 인스턴스 : 객체 = class명()을 나타내어 객체가 class안에 있는 메소드를 사용할 수 있다.

```python
class KoreanGreeting:
    # 클래스 필드
    Greeting = '안녕하세요'

    def __init__(self):
        # 인스턴스 필드
        self.show = self.Greeting

    @classmethod
    def class_greeting(cls):
        # cls는 인스턴스 필드를 참조하지 못해..
        return cls()

    @staticmethod
    def static_greeting():
        return KoreanGreeting()

    def is_greeting(self):
        print(self.show)


class EnglishGreeting(KoreanGreeting):
    Greeting = 'Hello'

K = EnglishGreeting.class_greeting()
E = EnglishGreeting.static_greeting()

K.is_greeting()
E.is_greeting()
```

위와 같이 먼저, @staticmethod는 특별히 추가되는 인자는 없기때문에, 상속에서 @classmethod와는 다르게 부모클래스로부터 속성의 값을 가져온다. 그래서, 출력값은 ' 안녕하세요'가 나오고 @classmethod는 cls인자를 가져와 클래스속성을 가져오기 때문에, 출력값은 'Hello'가 나온다.

### try catch
### lambda (무명메소드)
### 싱글톤패턴
### 추상클래스 (import abc)
### 동기 / 비동기
### 제너레이터
### 데코레이터
### 코루틴
### pyQt Framework
### Django Framework

## Homework
### 자판기 만들기

파이썬을 이용하여 자판기를 만들어 보았다.

```python
class VendingMachine:
    def __init__(self):
        self.drink_menu = {1: ('레몬', 500), 2: ('물', 600), 3: ('환타', 700), 4: ('커피', 1000)}
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
            return False
        elif answer == '아니요':
            return True
 ```
 
 + init은 initialize의 줄임말로 초기화란 뜻을 나타낸다. 파이썬에서 스페셜메소드를
먼저 class VendingMachine으로 객체의 타입을 정한다. init함수(method)안에 음료수메뉴와 돈을 설정한다. self.money = 0으로 설정한 이유는 돈을 얼마를 넣을지 모르기 때문이다. 자판기를 이용할 때, 돈을 넣으면 메뉴가 보이고 메뉴를 선택해서 선택한 물건을 받는다. 그래서, 음료수의 메뉴와 돈을 설정했으니, 돈을 넣는 함수(method)가 필요해서 input함수를 넣었다. 문자가 아닌 숫자로 계산해야 되기 때문에, int함수(method)를 사용해서, int함수(method)에서 출력한 값을 self.money와 더해준다. 돈을 넣는 함수(method)를 만들었으니, 메뉴를 보여줘야 한다. show_menu함수(method)에서 메뉴를 일일히 쓸 필요없이 숫자로 쓰고 싶어서, 음료수메뉴의 딕셔너리(dict)key값을 menus로 받는다. 복수인 이유는 메뉴가 한가지가 아니기 때문에, 복수형이다. menus를 for문으로 이용하여, self.drink_menu[menu]을 메뉴이름과 비용의 리스트로 출력하여 음료번호. 음료, 비용을 포맷함수를 써서 표현한다. select함수(method)에서는 메뉴를 선택해야한다. init함수에 있는 딕셔너리에 숫자를 key로 잡은 이유가 select함수에서 나온다. 번호로 선택해야 하기 때문에, int함수를 쓰고, self.drink_menu[_idx]을 메뉴이름과 비용의 리스트로 출력해서 리턴(return)값으로 반환해준다.
### 엘레베이터 (콘솔버전)
### 엘레베이터 (pyQt - GUI)
### 웹 크롤러 (Selenium, pyQt, Django)
