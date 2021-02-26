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

반복해서 사용할 때 while문이 필요하다. 예를 들어, 음악재생을 100번하고 싶다고 하면,
```python
song_play = 0
while song_play < 100:
  song_play = song_play+1
  print('노래를 %d번 재생합니다' %song)
 ```
 
 음악재생 100번 재생할 때 까지 계속 반복된다. 만약에 음악재생를 50번째에서 멈추고 싶다면
 ```python
song_play = 0
while song_play < 100:
  song_play = song_play+1
  print('노래를 %d번 재생합니다' %song)
  if song_play == 50:
    print('재생을 멈춥니다.)
    break
 ```
 위와 같은 break문으로 50번째에서 음악재생을 멈출 수 있다.

### 리스트(list)

리스트는 영어 뜻 그대로 목록이고, 순서가 있는 수정가능한 객체이다. 리스트는 대괄호([]) 표현을 한다.

```python
l1 = [1, 2, 2, 3, 4, 5]
l1.count(2)
l1.append(8)
l1.insert(4, 2)
l1.sort()
print(l1)
print(l1.count(2))
l1.count(8)
print(l1.count(8))

l2 = [1, 2, 3, 4]
l2.reverse()
l2.remove(2)
l2.pop(0)
l2.extend([2, 9])
print(l2)
```
위에서 보면 append는 l1이라는 리스트에 8을 추가하겠다는 뜻이다. count는 l1의 리스트에 중복된 2라는 숫자의 수를 알 수 있다. insert는 l1의 4번째 열(index)에 2를 삽입하겠다는 뜻이다. sort는 l1의 리스트를 순서대로 정돈해준다. reverse는 l2의 리스트의 목록을 거꾸로 전환해준다. remove는 요소제거해준다. 그래서, l2리스트에 2를 제거해주는 것을 확인할 수 있다. pop은 열의 0번째를 삭제해주었다. extend는 말그대로 확장이라는 뜻이다. l2리스트에 2, 9라는 숫자를 리스트에 추가해주었다.

### 딕셔너리(dict)

딕셔너리란 사전이란 뜻이고, **key와 value를 한쌍**으로 갖는다.

```python
animal = {'육식동물':'호랑이', '초식동물':'기린'}
print(animal['육식동물'])
animal = {'육식동물':'호랑이', '육식동물':'사자'}
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

함수란, **입력값**(input, parameter, argument)을 가지고 어떤 일을 수행한 다음에 그 결과물을 내어놓는 것이다. 프로그래밍 코드를 작성하다보면 반복되는 코드를 줄여주기 위해 특정 코드를 함수안에 정의하고, 그 코드를 함수명칭을 호출함으로써 코드를 실행하게 해준다.(**재사용성** 및 **가독성**증가) 또, 함수를 사용하는 또 다른 이유는 자신이 만든 프로그램을 함수화하면 프로그램 흐름을 일목요연하게 볼 수 있기 때문이다. 마치 공장에서 원재료가 여러 공정을 거쳐 하나의 상품이 되는 것처럼 프로그램에서도 입력한 값이 여러 함수를 거치면서 원하는 결괏값을 내는 것을 볼 수 있다. 이렇게 되면 프로그램 흐름도 잘 파악할 수 있고 오류가 어디에서 나는지도 바로 알아차릴 수 있다. 함수의 구조를 예를 들면,
```python
def mul(a, b): 
    if a < b:
        print('식은 성립하지 않는다.')
    else:
        print('식은 성립한다.')
    return a*b
number = mul(a=2, b=20)
print(number)
```
위와 같이 곱하기(multiplication)의 함수를 사용해서 출력했다.

### 인덱스 슬라이싱
### Comprehension
### 상속
### 접근제한자
### 정적메소드 (@staticmethod, @classmethod)
### 추상클래스 (import abc)
### 동기 / 비동기
### 제너레이터
### 데코레이터
### 코루틴
### pyQt Framework
### Django Framework

## Homework
### 자판기 만들기
### 엘레베이터 (콘솔버전)
### 엘레베이터 (pyQt - GUI)
### 웹 크롤러 (Selenium, pyQt, Django)
