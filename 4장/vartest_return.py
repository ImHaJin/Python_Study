#함수 안에서 함수 밖의 변수를 변경하는 방법

#1. return 이용하기
a = 1
def vartest(a):
	a = a+1
	return a
	
print(vartest(a))

a = vartest(a)
print(a)


	