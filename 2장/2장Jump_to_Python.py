#고급문자열 포매팅

'''
문자열의 format함수를 이용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다. 
앞에서 살펴본 문자열 포매팅 예제들을 format함수를 이용해서 다음과 바꾸면 된다.
'''

#숫자 바로 대입하기
a = "I eat {} apples".format(3)
print(a)

#문자열 바로 대입하기
b = "I eat {} apples".format("five")
print(b)

#숫자 값을 가진 변수로 대입하기
number = 3
c = "I eat {} apples".format(number)
print(c)

#2개 이상의 값 넣어보기
numberr = 4
day = 2
d = "I ate {0} apples. so i was sick for {1} days".format(numberr,day)
print(d)

'''
이름으로 넣기
{name}형태를 이용하는 방법도 있다. 이 형태를 이용할 경우 format 함수의 입력값에는 
반드시 name=value와 같은 형태의 입력값이 있어야 한다.
'''
e = "I ate {num} apples. so i was sick for {day} days".format(num=2,day=2)
print(e)

#인덱스와 이름을 혼용해서 넣기
f = "I ate {0} apples. so i was sick for {day} days".format(50,day=20)
print(f)

#왼쪽 정렬
g = "{0:<10}".format("hi")
print(g)

#오른쪽 정렬
h = "{0:>10}".format("hi")
print(h)

#가운데 정렬
i = "{0:^10}".format("hi")
print(i)

#공백 채워넣기
j = "{0:=^10}".format("보고싶어")
print(j)
k = "{0:*^10}".format("잘지내라")
print(k)

#소수점 표현하기
l = 925.1923
print("{0:0.4f}".format(l))
print("{0:10.4f}".format(l))

#{'또는'} 문자 표현하기
print("{{문자 그대로 사용하기}}".format())




