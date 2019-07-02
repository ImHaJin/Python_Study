#파일에 새로운 내용 추가하기
#원래 있던 값을 유지하면서 새로운 값을 추가해야 할 경우도 있다.

f = open("C:/Python_Study/새파일.txt","a")
for i in range(11,20):
	data = "%d번째 줄입니다. \n" %i
	f.write(data)
f.close()

