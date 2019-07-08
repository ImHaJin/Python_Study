def sum(a,b):
	return a+b

def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	return a/b

def rem(a,b):
	return a%b

print("="*30)
print("1.더하기\n2.빼기\n3.곱하기\n4.나누기\n5.나머지 구하기")
print("="*30)

while True:
	menu = int(input("원하는 계산기 기능을 입력하세요."))
	if(menu <= 5):
		numA = int(input("첫번 째 숫자를 입력하세요"))
		numB = int(input("두번 째 숫자를 입력하세요"))
		if(menu == 1):
			result = sum(numA, numB)
			print("결과는 %d입니다." %result)

		elif(menu == 2):
			result = sub(numA, numB)
			print("결과는 %d입니다." %result)
		
		elif(menu == 3):
			result = mul(numA, numB)
			print("결과는 %d입니다." %result)
		
		elif(menu == 4):
			result = div(numA, numB)
			print("결과는 %d입니다." %result)

		elif(menu == 5):
			result = rem(numA, numB)
			print("결과는 %d입니다." %result)
	elif(menu == 6):
		break
	else:
		print("잘못 입력하셨어요. 다시 입력해주세요.")
