'''
	자료형의 참과 거짓
자료형에도 참과 거짓이 있다. 
'''

#마지막 요소를 끄집어내는 함수(pop)
a = [1,2,3,4]
while a:
	print(a.pop())

if []:
	print("True")
else:
	print("False")

#만약 [1,2,3]이 참이면 "True"라는 문자를 출력하고 그렇지 않으면 "False"을 출력하라.
if[1,2,3]:
	print("True")
else:
	print("False")

