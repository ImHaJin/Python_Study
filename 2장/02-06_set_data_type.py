'''
	집합 자료형은 어떻게 만들까?
집합 자료형은 set키워드를 이용해 만들 수 있다.
'''

s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

'''
	집합 자료형의 특징 
s2 = set("Hello") 출력해보니 l문자가 하나 빠져있고 순서도 뒤죽박죽이다. 왜 그럴까?
set에는 다음과 같은 2가지 특징이 있다.
1. 중복을 허용하지 않는다.
2. 순서가 없다.
'''

#set자료형을 리스트형으로 변환하기
s1 = set([1,2,3])
l1 = list(s1)
print(l1)

t1 = tuple(s1)
print(t1)
print(t1[0])

'''
	집합 자료형 활용하는 방법
set자료형이 정말 유용하게 사용되는 경우는 다음과 같이 교집합/합집합/차집합을 구할 때이다.
'''

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#교집합 / &를 사용해도 되고 intersection함수를 사용해도 된다.
print(s1&s2)
print(s1.intersection(s2))

#합집합 / |를 사용해도 되고 union함수를 사용해도 된다.
print(s1|s2)
print(s1.union(s2))

#차집합 / -를 사용해도 되고 difference함수를 사용해도 된다.
print(s1-s2)
print(s2-s1)
print(s1.difference(s2))

#집합 자료형 관련 함수들
#값 1개 추가하기(add)
s1 = set([1,2,3])
print(s1)
s1.add(4)
print(s1)

#값 여러 개 추가하기(update)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

#특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
print(s1)