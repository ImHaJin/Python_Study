'''
	if문을 배워보자 !
'''

money = 1
if money :
	print("택시타고 집 가자!")	
else: 
	print("돈업으면 걸어가!")

'''
	비교연산자
<  >  ==  !=  >=  <=
'''

#만약 3000원 이상의 돈을 가지고 있으면 택시틀 타고 그렇지 않으면 걸어가라
money = 2000
if money >= 3000:
	print("택시타고 가라!")
else: 
	print("걸어가 !")


'''
	조건을 판단하기 위한 연산자
and  or  not
'''

#돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라
money = 2000
card = 1
if money >= 3000 or card: 
	print("택시 타고 집에 가자")
else: 
	print("걸어가")
	
'''
	파이썬에서 제공하는 재미있는 조건들
x in s / x not in s
'''

#1이 [1,2,3]안에 있는가?
1 in [1,2,3]

#1이 [1,2,3]안에 없는가?
1 not in [1,2,3]

#튜플을 이용한 예
print('a' in ('a','b','c'))
#문자열을 이용한 예
print('good' not in "너무 졸려 하지만 잘 수 없엉")

life = ["현실적", "성격" ,"돈"]

if '외모' in life:
	print("현실적으로 생각을 잘하넴?")
else:
	print("외모는 일시적일 뿐 물론 잘생기면 좋지 !")

#조건문에서 아무 일도 하지 않게 설정하고 싶다면? pass를 이용하자!
life = ["현실적", "성격" ,"돈"]

if '성격' in life:
	pass
else:
	print("외모는 일시적일 뿐 물론 잘생기면 좋지 !")


#다양한 조건을 판단하는 elif
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket: 
	print("택시를 타고 가라")
elif card: 
	print("택시를 타고 가라")
else:
	print("걸어가")

#if문을 한줄로 작성하기. 때때로 이런 방식으로 하는게 편할 수 있다.
pocket = ['paper', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")





