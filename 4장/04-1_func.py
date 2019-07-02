'''
	함수
입출력이 중요하다.
'''

#파이썬 함수의 구조
#이 함수의 이름은 sum이고 입력 인수로 2개이고, 결과값은 2개의 입력값을 더한 값이다.
def sum(a,b):
	return a+b

#sum 함수 사용해보기
a = 3 
b = 4
c = sum(a,b)
print(c)

'''
	입력값과 결과값에 따른 함수의 형태
함수의 형태는 입력값과 결과값의 존재 유무에 따라 4가지 유형으로 나뉜다.
'''

#1. 일반적인 함수
def sum(a,b):
	result = a + b
	return result

#2. 입력값이 없는 함수
#이처럼 입력값이 없고 결과값만 있는 함수는 다음과 같이 사용된다. → 결과값을 받을 변수 = 함수명()
def say():
	return 'Hi'
say = say()
print(say)

#3. 결과값이 없는 함수
#결과값이 있는 것처럼 착각하지마. print로 찍힌 것일뿐. 결과값은 return으로만 받을 수 있다.
def sum(a,b):
	print("%d, %d의 합은 %d입니다." % (a,b,a+b))
sum(3,4)

#3번에 대한 결과값이 있는지 확인해보자
a = sum(3,4)
print(a)

#4. 입력값도 결과값도 없는 함수
def say():
	print("hi")

#입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
#이런 문제를 해결하기 위해서 →def 함수명(*입력 변수): 수행할문장/ 으로 제공한다.

#여러 개의 입력값을 받는 함수 만들기
def sum_many(*args):
	sum = 0
	for i in args:
		sum = sum+i
	return sum

result = sum_many(1,2,3)
print(result)
result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def sum_mul(choice, *args):
	if choice == "sum" :
		result = 0
		for i in args:
			result = result + i
	elif choice == "mul" :
		result = 1
		for i in args: 
			result = result * i
	return result

result = sum_mul('sum',1,2,3,4,5) 
print(result)

result = sum_mul('mul',1,2,3,4,5)
print(result)

#함수의 결과값은 언제나 하나이다.
#오류가 발생할까요? No~ 결과값은 하나다! a+b와 a*b는 튜플값 하나인 (a+b,a*b)를 돌려준다.
def sum_and_mul(a,b):
	return a+b, a*b

result = sum_and_mul(3,4)
print(result)

sum, mul = sum_and_mul(3,4)
print(sum,mul)

#그럼 return문을 2번 사용하면 2개의 결과값을 돌려주지 않을까? 하지만 파이썬에서 이와 같은 함수는 참 어리석은 함수다.
#하나의 return문을 만나는 순간 결과값을 돌려주고 다음 함수를 빠져나가게 된다.
def sum_and_mul(a,b):
	return a+b
	return a*b

print(sum_and_mul(2,3))

#return의 또 다른 쓰임새
#출력되는건 print다. return값이 아닌 것을 명심하자. 이처럼 return으로 함수를 빠져나가는 방법은 실제 프로그래밍에서 자주 쓰인다.
def say_nick(nick):
	if nick == '바보':
		return
	print('나의 별명은 %s입니다.' %nick)

say_nick('frog')
say_nick('바보')

#입력 인수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
	print('나의 이름은 %s입니다.' %name)
	print('나의 이름은 %d입니다.' %old)
	if man:
		print('남자입니다')
	else: 
		print('여자입니다')

say_myself('Carl',28,False)
say_myself('Carl',28,True)

'''
초깃값을 설정해놓은 입력 인수값은 맨 뒤쪽에 위치시키자.
def say_myself2(name, man=True, old):
	print('나의 이름은 %s입니다.' %name)
	print('나의 이름은 %d입니다.' %old)
	if man:
		print('남자입니다')
	else: 
		print('여자입니다')
'''



