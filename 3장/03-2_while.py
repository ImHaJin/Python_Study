'''
	while문을 배워보자 !
while문은 조건문이 참인 동안에 while문 아래에 속하는 문자들이 반복해서 수행된다.
'''

'''
#'열 번 찍어 안 넘어가는 나무 없다' 속담 만들어보기
treeHit = 0 # 나무를 찍은 횟수
while treeHit < 10:
	treeHit = treeHit + 1
	print("나무를 %d번 찍었습니다" %treeHit)
	if treeHit == 10:
		print("나무가 넘어갑니다.")
print("-------------------------------")

#while문 직접 만들기
prompt = """
1. ADD
2. Del
3. List
4. Quit
Enter number:"""

number = 0 #번호를 입력받을 변수
while number !=4:
	print(prompt)
	number = int(input())
	
#while문 강제로 빠져나가기
#커피 자판기를 만들어보자
coffee = 10
money = 300
while money: 
	print("돈 받았으니 커피를 주자.")

	coffee = coffee - 1
	print("남은 커피의 양은 %d잔입니다." %coffee)

	if not coffee:
		print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
		break
'''

#조건에 맞지 않는 경우 맨 처음으로 돌아가기
#while문 안의 문장을 수행할 때, 입력된 조건을 검사해서 조건에 맞지 않으면 while문을 빠져나간다.
#그런데 while문을 빠져나가지 않고 while문의 맨 처음으로 다시 돌아가게 하고 싶다면? contunue를 사용하자

a = 0
while a < 10:
	a = a+1
	if a % 2 == 0: continue
	print(a)
	
#while문 무한 루프를 조심합시다.




