'''
	내장함수
파이썬이 기본적으로 제공하는 내장 함수들은 외부 모듈과는 달리 import를 필요로 하지 않는다.
활용빈도가 높고 중요한 함수들을 알파벳 순서대로 정리했으니, 한 번 살펴보자.
'''

#abs() / 어떤 숫자를 입력으로 받았을 때, 그 숫자의 절대값을 돌려주는 함수
print(abs(3))
print(abs(-3))
print(abs(-1.2))
print('-------------------------')

#all() / 반복 가능한 자료형 x를 입력 인수로 받으며, 이 x가
print(all([1,2,3]))
print(all([1,2,3,0]))
print('-------------------------')

#any(x) / x 중 하나라도 참이 있을 경우 True를 리턴하고, x가 모두 거짓일 경우에만 False를 리턴한다.
print(any([1,2,3,0]))
print(any(["",0]))
print('-------------------------')

#chr() / 아스키 코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수이다.
print(chr(97))
print(chr(48))
print('-------------------------')

#dir() / 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
print(dir([1,2,3]))
print('-------------------------')
print(dir({'1':'0'}))
print('-------------------------')

#divmod(a,b) / 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴하는 함수다.
print(divmod(301,2))

#enumerate 열거하다 / 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
for i, name in enumerate(['body', 'foo', 'bar']):
	print(i,name)
print('-------------------------')

#eval / 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 리턴하는 함수이다.
#보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶은 경우에 사용된다.
print(eval('10+20'))
print(eval("'안'+'녕'"))
print(eval('divmod(40,3)'))

#hex / 정수값을 입력받아 16진수로 변환하여 리턴하는 함수
print(hex(234))
print(hex(3))

#id(object) / 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 리턴하는 함수이다.
a = 3
print(id(3))
print(id(a))

b = a 
print(id(b))
print('-------------------------')

#input / 사용자 입력을 받는 함수이다.
#c = input("Enter:")

#int / 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 리턴하는 함수로, 정수를 입력으로 받으면 그대로 리턴한다.
print(int('3'))
print(int(4.3))

#int(x,raidx)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴한다.
print(int('11',11))
print(int('1A',30))
print('-------------------------')

#isinstance(object, class) / 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 리턴한다.
class Person: pass

a = Person()
print(isinstance(a, Person))
print('-------------------------')

#lambda / 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다. 람다는 def보다 더 간결하게 사용할 수 있다. 익숙해지면 편리해짐
sum = lambda a,b: a+b
print(sum(3,4))

myList = [lambda a,b:a+b, lambda a,b: a*b]
print(myList)
print(myList[0](10,20))
print(myList[1](10,20))
print('-------------------------')

#len / 반복 가능한 자료형 s를 입력받아 리스트로 만들어 리턴하는 함수이다.
print(list('python'))
print(list((1,2,3)))
d = [1,2,3]
e = list(d)
print(d)
print('-------------------------')

#map(f,iterable) / 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. 
#map은 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수다.
print('-------------------------')

#max(iterable) / 인수로 반복 가능한 자료형을 입력받아 그 최대값을 리턴하는 함수이다.
print(max([1,2,3]))
print(max('python'))
print('-------------------------')

#min(iterable) / max함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최소값을 리턴하는 함수이다. 
print(min([1,2,3]))
print(min('python'))
print('-------------------------')

#oct(x) / 정수 형태의 숫자를 8진수 문자열로 바꾸어 리턴하는 함수이다.
print(oct(34))

#open(filename, [mode]) '파일 이름'과 '읽기 방법'을 입력받아 파일 객체를 리턴하는 함수이다.
#f = open("mod1.py", "rb")
#fread = open("read_mode.txt","r")
print('-------------------------')

#ord(c) / 문자의 아스키 코드값을 리턴하는 함수이다.
print(ord('a'))
print(ord('0'))

#pow(x,y) / x의 y제곱한 값이다.
print(pow(5,3))

#range([start,] stop [,step]) / for문과 자주 사용된다. 
#이 함수는 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴한다.

#인수가 하나일 경우 / 시작 숫자를 지정해주지 않으면 range함수는 0부터 시작한다.
print(list(range(5)))
#인수가 2개일 경우
print(list(range(5,10)))
#인수가 3개일 경우 / 숫자 사이의 거리를 말한다.
print(list(range(5,10,2)))
print('-------------------------')

#sorted(iterable) / 입력값을 정렬한 후 그 결과를 리스트로 리턴하는 함수이다.
#sort함수는 리스트 객체를 정렬하지만 정렬된 결과를 리턴하지는 않는다.
print(sorted([3,2,1]))

abc = [1,2,3]
result = abc.sort()
print(result)
print(abc)
print('-------------------------')

#str(object) / 문자열 형태로 객체를 변환하여 리턴하는 함수이다.
print(str(3))
print(str('문자로 취급'))
print(str('hi'.upper()))
print('-------------------------')

#tuple(iterable) / 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 리턴하는 함수다.
#만약 튜플이 입력으로 들어오면 그대로 리턴한다.

print(tuple("mother"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))
print('-------------------------')

#type(object) / 입력값의 자료형이 무엇인지 알려주는 함수이다.
print(type("ac"))
print(type([]))
print(type(open("test",'w')))
print('-------------------------')

#zip(iterable*) / 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수이다.
print(list(zip([1,2,3],[4,5,6])))








print('-------------------------')
print('-------------------------')



