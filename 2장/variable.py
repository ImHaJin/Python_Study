import sys
from copy import copy

'''
	변수란?
파이썬에서 사용하는 변수는 객체를 가리키는 것
파이썬의 모든 자료형은 객체라고 한다.
'''

a = 5
b = "python"
c = [1,2,3]

print(type(3))

print(a is "b")
print(a is b)

#입력한 자료형에 대한 참조 개수를 알려주는 sys.getrefcount()
print(sys.getrefcount(5))

print("----------------------------------------")

#변수를 만드는 여러가지 방법
a,b= {'python','life'}
print(b)

(a,b) = 'python','life'
print(a)
print(b)

#리스트로 변수 만들기
[a,b] = ['python','life']
print("----------------------------------------")

#여러 개의 변수에 값은 값을 대입할 수도 있다.
a = b = 'python'
print(a)

#두 변수의 값을 간단히 바꾸기 
a = 3
b = 5
a,b = b,a
print(a)
print(b)

#메모리에 생성된 변수 없애기

a = 3
b = 3
del(a)
del(b)

#리스트를 변수에 넣고 복사하고자 할 때
a = [1,2,3]
b = a
a[1] = 4
print(a)
print("---------------------")

#b변수를 생성할 때 a와같은 값을 가지도록 복사해 넣으면서 a가 가리키는 리스트와는
#다른 리스트를 가리케 하는 방법은? 2가지가 있다.
# 1.[:] 이용하기 2. copy 모듈 이용
a = [1,2,3]
b = a[:]
c = copy(a)
a[1] = 4
print(a)
print(b)
print(c)
print("---------------------")

#동일한 객체인지 확인해보기
print(b is a)
print(a is b)
print(b is c)


