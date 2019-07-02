#함수 안에서 선언된 변수의 효력범위
a = 3
def vartest(a):
	a = a+3

vartest(a)
print(a)

def vartest1(hello):
	hello = hello+1


