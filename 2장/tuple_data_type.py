'''
	튜플 자료형
튜플은 몇가지 점을 제외하곤 리스트와 거의 비슷하다.
1. 리스트는 [과]으로 둘러싸지만, 튜플은 (과)으로 둘러싼다.
2. 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
튜플의 모습
t1 = ()
t2 = (1,) 1개의 요소만을 가질 땐 ,를 붙여 한다.
t3 = (1,2,3)
t4 = 1,2,3   ()를 생략해도 무방하다.
t5 = ('a','b',('ab','cd'))
'''

#그렇다면 튜플의 요소값을 지우거나 변경하려고 하면 무슨 일이 일어날까?
#t1 = (1,2,'a','b')
#del t1[0] #오류가 터지죠~ 지울 수가 없어요 ! 마찬가지로 변경도 안되요 ! 
#t1[0] = 'c'

#튜플의 인덱싱과 슬라이싱, 더하기와 곱하기를 해보자
t1 = (1,1,2,'a','b')

#인덱싱하기
print(t1[2])

#슬라이싱하기
print(t1[1:])

#더하기
t2 = (3,4,)
print(t1+t2)

#튜플 곱하기
print(t2*t1.count(1))
print(t2*3)


