#global 명령어 이용하기
#global명령어는 함수 안에서 함수 밖의 a변수를 직접 사용하겠다는 뜻이다.
#외부 분수에 종속적인 함수는 좋지 않으므로 웬만하면 쓰지말자. 
a = 1
def vartest():
	global a
	a = a+1

vartest()
print(a)
