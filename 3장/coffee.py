#break문 이용해 자판기 작동 과정 만들기
coffee = 10
while True:
	money = int(input("돈을 넣어주세요."))
	if money == 300:
		print("커피를 줍니다.")
		coffee = coffee - 1
		print(coffee)
		print("-------------------------------------")
	elif money > 300:
		print("거스름돈 %d원을 주고 커피를 줍니다." %(money-300))
		coffee = coffee - 1
		print(coffee)
		print("-------------------------------------")
	else: 
		print("돈을 다시 돌려주고 커피를 주지 않습니다.")
		print("남은 커피의 양은 %d개입니다." %coffee)		
	if not coffee:
		print("커피가 다 떨어졌어요.")
		break



	

