#파일을 쓰기 모드로 열어 출력값 적기
f = open("C:\Python_Study\새파일.txt",'w')
for i in range(1,11):
	data = "%d번째 줄입니다. \n" %i
	f.write(data)
f.close()

for i in range(1,10):
	data = "%d번째 줄입니다. \n" %i
	print(data)
f.close()

