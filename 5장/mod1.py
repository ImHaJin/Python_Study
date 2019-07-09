'''
	모듈이란?
모듈이란 함수나 변수 또는 클래스들을 모아 놓은 파일이다.
모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만드렁진 파이썬 파일이라고도 할 수 있다.

###
import의 사용방법 → import 모듈이름

###
모듈 함수를 사용하는 또 다른 방법
→ 1.from 모듈이름 import 모듈함수 2.from 모듈이름 import 모듈함수,모듈함수 3.from 모듈이름 import *
ex) from mod1 import sum 
'''

def sum(a,b):
	return a+b

def safe_sum(a,b):
	if type(a) != type(b):
		print("객체 a와 객체 b는 더할 수 있는 것이 아닙니다.")
		return #반환값은 None을 반환해준다.
	else:
		result = sum(a,b)
	return result

#if __name__ == "__main__":의 의미 → 실행되지 않는다.
if __name__ == "__main__":
	print(safe_sum('a',1))
	print(safe_sum(1,4))
	print(sum(10, 10.4))

#클래스나 변수 등을 포함한 모듈




	