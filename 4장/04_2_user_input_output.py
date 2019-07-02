
'''
	사용자 입력
'''

#사용자 입력값 받기(input)
a = input()
print(a)

#프롬프트를 띄워서 사용자 입력 받기
input("질문 내용이 어떻게 되시나요?")

number = input("숫자를 입력하세요:")
print(number)

'''
	print 자세히 알기
우리는 여태 입력한 자료형 출력하는 기능만 알았다. 다른 기능을 알아보자.
'''

#큰따옴표(")로 둘러싸인 문자열은 +연산과 동일하다.
print("life""is""good")
print("life"+"is"+"good")

#문자열 띄어쓰기는 콤마로 한다.
print("life","is","good")

#한 줄에 결과값 출력하기(end)
for i in range(10):
	print(i, end=' ')
	








