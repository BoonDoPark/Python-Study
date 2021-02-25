# Python
Learning Python
※ 모듈 사용 (copy, datetime, pandas, os, openpyxl, pickle, json, Selenium ..)

## Course

###클래스(class)

클래스란 코딩을 시작하기 전에 틀을 짜는 것을 의미한다. 클래스의 명칭에 따라 코딩의 주제가 바뀌기 때문에 클래스명에 신경을 많이 써야한다.
```python
class 생성자:
```
위와 같이 클래스를 지정 후 코딩을 해야한다.

###while문, break문

반복해서 사용할 때 while문이 필요하다. 예를 들어, 음악재생을 100번하고 싶다고 하면,
```python
song_play = 0
while song_play < 100:
  song_play = song_play+1
  print('노래를 %d번 재생합니다' %song)
 ```
 음악재생가 100번 재생할 때 까지 계속 반복된다. 만약에 음악재생를 50번째에서 멈추고 싶다면
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

###리스트(list)

리스트는 영어 뜻 그대로 목록이고, 순서가 있는 수정가능한 객체이다. 리스트는 []이걸로 표현을 한다.
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
###딕셔너리(dict)

###for in 반복문

###함수(function)

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
