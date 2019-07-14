'''
	예외 처리	
오류를 무시하고 싶을 때도 있다. 이에 파이썬은 try, except를 이용해서 예외적으로 오류를 처리할 수 있다.
'''

#f = open("나 없는 파일", 'r')
#a = [1,2,3]
#print(a[3])

'''
	오류 예외 처리 기법
try:
	...
except[발생오류[as 오류 메시지 변수]]:
	...
- 위 구문에서 []기호를 사용하는데 이 기호는 괄호 안의 내용을 생략할 수 있다.
except구문은 다음처럼 3가지 방법으로 사용할 수 있다.

1. try, except만 쓰는 방법
try:
	...
except:
	...

2. 발생 오류만 포함한 except문
try:
	...
except 발생오류:
	...

3. 발생 오류와 메시지 변수까지 포함한 except문
try:
	...
except 발생 오류 as 오류 메시지 변수:
'''

try:
	4/0
except ZeroDivisionError as e:
	print(e)

#try ..else 
#else절은 예외가 발생하지 않은 경우 실행되며 반드시 except절 바로 다음에 위치해야 한다.
try:
	f = open('foo.txt','r')
except FileNotFoundError as e:
	print(str(e))
else: 
	data = f.read()
	f.close()

#try ..finally
#try문에는 finally절을 사용할 수 있다. finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
#보통 finally절은 사용한 리소스를 close해야 할 경우에 많이 사용된다.

'''
f = open('foo.txt', 'w')
try: 
	#무언가를 수행한다.
finally:
	f.close()
'''

#오류 회피하기
#특정오류가 발생했을 때, 그냥 넘겨야할 경우도 있다.
try: 
	f = open("나없는 파일",'r')
except FileNotFoundError:
	pass


#오류 일부러 발생시키기(raise)
#이상한 소리로 들리겠지만, 프로그래밍을 하다보면 종종 오류를 발생시켜야 할 경우도 생긴다.
class Bird:
	def fly(self):
		#raise NotImplementedError
		print("정상 월급 좀 받아서 날아보자 제발~")

class Eagle(Bird):
	pass
 
eagle = Eagle()
eagle.fly()