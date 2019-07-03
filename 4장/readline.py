'''
	프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
파이썬에는 외부 파일을 읽어 들여 프로그램에서 사용할 수 있는 여러가지 방법이 있다.
'''

#readline() 함수 이용하기
'''
f = open("C:/Python_Study/새파일.txt","r")
line = f.readline()
print(line)
f.close()


#모든 라인 읽어들이기(파일을 이용한 입력방법)
f = open("C:/Python_Study/새파일.txt","r")
while True:
	line = f.readline()
	if not line: break
	print(line)
f.close()

#키보드를 이용한 입력방법
f = open("C:/Python_Study/새파일.txt","r")
while True:
	data = input()
	if not data:break
	print(data)
f.close()


#readlines() 함수 이용하기
#lines는 리스트가 된다.
f = open("C:/Python_Study/새파일.txt","r")
lines = f.readlines()
for line in lines:
	print(line)
f.close()
'''

#read() 함수 이용하기
#파일의 내용 전체를 문자열로 리턴한다.
f = open("C:/Python_Study/새파일.txt","r")
data = f.read()
print(data)
f.close()




