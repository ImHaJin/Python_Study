'''
	박씨네 집 클래스 예제를 만들어보자.
'''

class HousePark:
	lastname = "박"
	
	def __init__(self, name):
		self.fullname = self.lastname + name
	def travel(self, where):
		print("%s, %s여행을 가다" %(self.fullname, where))
	def love(self, other):
		print("%s, %s이 사랑에 빠졌네~" %(self.fullname, other.fullname))
	def __add__(self, other):
		print("%s, %s 결혼했네~" %(self.fullname, other.fullname))
	def fight(self, other):
		print("%s, %s 싸우네" %(self.fullname, other.fullname))
	def __sub__(self, other):
		print("%s, %s 이혼하네" %(self.fullname, other.fullname))
'''
pey = HousePark()
pey.setname("응용")
pey.travel("부산")
pey.travel("태국")
print("------------------------")
print(pey.lastname)
print(pey.fullname)
'''

#초기값 설정하기 
pey = HousePark("응용")
pey.travel("부산")

#클래스의 상속 → class 상속받을 클래스명(상속할 클래스명)

''' 
	메서드 오버라이딩
상속의 개념 중 한가지 더 알아야하는 것이 있다. 클래스를 만들다 보면 상속받을 대상이 클래스의
메서드와 이름은 같지만 그 행동을 다르게 해야 할 때가 있다. 이럴 때는 어떻게 해야 할까?
→ 메서드 이름을 동일하게 다른 행동으로 구현하기
'''

'''
	연산자 오버로딩
연산자(+, -, *, / 등)를 객체끼리 사용할 수 있게 하는 기법이다.
'''

class HouseKim(HousePark):
	lastname = "김"

	def travel(self, where, day):
		print("%s, %s여행을 %d일 동안 가다" %(self.fullname, where, day))

carl = HouseKim("Carl")
carl.travel("독도", 3)
pey.love(carl)
pey + carl

'''
	'박씨네 집' 클래스 완성하기
스토리 라인 : 박응용은 부산에 놀러가고 ~
Carl도 우연히 3일 동안 부산에 놀러 간다.
둘은 사랑에 빠져서 결혼한다. 그러다가 바로 싸우고 이혼을 하게 된다.
'''

pey = HousePark("박응용")
carl = HouseKim("Carl")
pey.travel("부산")
carl.travel("부산", 3)
pey.love(carl)
pey+carl
pey.fight(carl)
pey-carl

