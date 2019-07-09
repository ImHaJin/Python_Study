#클래스나 변수 등을 포함한 모듈
#지금까지 살펴본 모듈은 함수만 포함했지만 클래스나 변수 등을 포함할 수도 있다.

PI = 3.141592
class Math:
	def solv(self, r): #반지름을 계산하는 클래스, r**2는 r제곱을 의미함.
		return PI * (r**2)

def sum(a,b):
	return a+b
		
if __name__ == "__main__":
	print(PI)
	a = Math()
	print(a.solv(2))
	print(sum(PI, 4.4))


