import sys

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
print(b)
