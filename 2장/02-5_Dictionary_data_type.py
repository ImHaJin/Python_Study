'''
	딕셔너리 자료형
사람은 "이름" = "홍길동", "생일" = "몇 월 몇 일" 등으로 구분할 수 있다.
파이썬은 이러한 대응관계를 나타낼 수 있는 자료형을 가지고 있다.
이러한 대응관계를 나타내는 자료형을 연관 배열 또는 해시라고 한다.
파이썬에서는 이러한 자료형을 딕셔너리라고 한다.(말 그대로 사전)
Key와 Value라는 한 쌍으로 갖는 자료형이다.
'''

#딕셔너리는 어떻게 만들까? / Ex) {Key1:Value1, Key2:Value2, Key3:Value3 }
#딕셔너리는 어떻게 만들까? / Ex) {'name':'하진', 'age':'28','birth':'0620'} 여기서 Key는 name/age/birth가 된다.
dic = {'name':'하진', 'age':'28','birth':'0620'}
print(dic.keys())
print(dic.values())

#Key로 정수값1, Value로 'hi'
a = {1:'hi'}

#Value에 리스트도 넣을 수 있다.
a = {'a':[1,2,3]}
print(a)
print('----------------------------------------------')

#딕셔너리 쌍 추가, 삭제하기 
#Tip! 딕셔너리는 순서를 따지지 않는다는 사실을 기억하자. 다음 예에서 알 수 있듯이 추가되는 순서는 원칙이 없다.
a = {1:'a'}
a[2] = 'b'
a[3] = 'c'
print(a)
print('----------------------------------------------')

a['name'] = '하진'
print(a)

a[3] = [1,2,3]
print(a)
print('----------------------------------------------')

#딕셔너리 요소 삭제하기
del a[1]
print(a)
print('----------------------------------------------')

#딕셔너리를 사용하는 방법을 알아보자.
'''
	딕셔너리에서 Key 사용해 Value를 얻어보자.
리스트나 튜플, 문자열은 요소값을 얻어내고자 할 때 인덱싱이나 슬라이싱 기법 중 하나를 이용했다.
하지만 딕셔너리는 단 한 가지 방법뿐이다. 바로 Key를 사용해서 Value를 얻어내는 방법이다.

'''
grade = {'pey':10, 'julliet':99}
print(grade['pey'])
print(grade['julliet'])

print('----------------------------------------------')
a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])

'''
	딕셔너리 만들 때 주의사항
먼저 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key값을 설정해 놓으면 
하나를 제외한 나머지 것들이 모두 무시된다는 점을 주의해야 한다.
1.중복되는 Key값을 절대로 쓰지 말자.
2.Key에는 리스트를 쓸 수 없다.
'''
exKey = {1:'a', 1:'b', 1:'c'}
print(exKey[1])
print('----------------------------------------------')

#exKey = {[1,2]:'화이팅'} / 리스트형 X

#딕셔너리 관련 함수들
#Key 리스트 만들기(keys)
dic = {'name':'하진', 'age':'28','birth':'0620'}
print(dic.keys())

#dict_keys객체는 리스트 고유의 함수인 append, insert, pop, remove, sort등의 함수를 사용할 수 없다.
for k in dic.keys():
	print(k)

#dict_keys객체를 리스트로 변환
print(list(dic.keys()))
print('----------------------------------------------')

#Value 리스트 만들기(values)
print(dic.values())
print('----------------------------------------------')

#Key, Value쌍 얻기(items)
print(dic.items())
print('----------------------------------------------')

#Key, Value쌍 모두 지우기(clear)
print(dic.clear())
print('----------------------------------------------')

#Key로 Value얻기(get)
dic = {'name':'하진', 'age':'28','birth':'0620'}
print(dic.get('name'))
print(dic.get('age'))
print('----------------------------------------------')

#print(a.get('nokey')) #None을 반환
#print(a['nokey'])

print(dic.get('foo','bar')) # key foo값이 없으니깐, default 'bar'를 리턴한다.

#해당 Key가 딕셔너리 안에 있는 조사하기(in)
dic = {'name':'하진', 'age':'28','birth':'0620'}
a = {1,2,3}
print('name' in dic)
print('name' in a)


