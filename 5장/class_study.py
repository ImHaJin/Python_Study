'''
	클래스 개념을 잡아보자.
마치 뽑기의 틀과 같다. 별 모양의 틀을 하나가 있다. 
이 틀은 클래스를 의미하고, 이 틀로 별 모양의 뽑기를 만들 수 있다. 별 모양의 뽑기는 인스턴스(=객체)를 말한다.
'''

#클래스의 간단한 예
class Simple:
	pass

#Simple클래스의 인스턴스를 만드는 방법
a = Simple()

#이야기 형식으로 클래스 기초를 쌓아보자. 순서대로 따라가보기.
#1. 클래스 변수

class Service:
	secret = "영구는 배꼽이 두 개다."

pey = Service()
print(pey.secret)

#2. 클래스 함수 
class Service: 
	secret = "영구는 배꼽이 두 개다."
	def sum(self, a, b):
		result = a + b
		print("%s + %s = %s입니다." %(a,b,result))

pey = Service()
pey.sum(1,1)

#self 간단히 살펴보기
#self 제대로 알기

class Service: 
	secret = "영구는 배꼽이 두 개다."
	def setname(self, name):
		self.name = name
	def sum(self, a, b):
		result = a + b
		print("%s님 %s + %s = %s입니다." %(self.name,a,b,result))

pey = Service()
pey.setname("임하진")
pey.sum(1,1)

#init이란 무엇인가?
#인스턴스를 만들 때 항상 실행된다.
class Service: 
	secret = "영구는 배꼽이 두 개다."
	def __init__(self, name):
		self.name = name
	def sum(self, a, b):
		result = a + b
		print("%s님 %s + %s = %s입니다." %(self.name,a,b,result))

#__init__함수 때문에, 아이디를 부여받을 때는 이처럼 입력해야한다.
pey = Service("Carl")
pey.sum(2,2)

'''
	클래스 자세히 알기
클래스란 인스턴스를 만들어내는 공장과도 같다. 
이 클래스로 우아하게 프로그램을 만들 수 있다. 예를 들어 자세히 알아보자.
'''
#사칙연산 클래스 만들기
#1. 클래스 구조 만들기
class FourCal:
	#2. 객체에 숫자 지정할 수 있게 만들기
	def setdata(self, first, second):
		self.first = first
		self.second = second

	def sum(self):
		result = self.first + self.second
		return result

	def mul(self):
		result = self.first * self.second
		return result
	def sub(self):
		result = self.first - self.second
		return result
	def div(self):
		result = self.first / self.second
		return result

#메서드의 또 다른 호출 방법 → FourCal.setdata(a,4,2) 이와 같이 '클래스명.메서드'형태로 호출할 땐 객체 a를 입력 인수로 넣어줘야한다.
#반면 '객체.메서드'형태로 호출할 때는 첫 번째 입력 인수(self)를 반드시 생략해야한다.
a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,7)

print(a.first, a.second)
print(b.first, b.second)
print(type(a))

print("---------------------------")
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())




