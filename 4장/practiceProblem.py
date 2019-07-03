'''
	함수문제
'''

#첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항들은 이전의 두 항을
#더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.
#입력을 정수 n으로 받았을 때, n이하까지의 피보나치 수열을 출력하는 함수를 작성해보자.

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n-2) + fib(n-1)
	
for i in range(10):
	print(fib(i),end=' ')


'''
	파일 읽고 쓰는 문제
'''

#총 10줄로 이루어진 sample.txt파일이 있다(70,60,55,75,95,90,80,80,85,100)
#다음 쪽을 보며, sample.txt파일의 숫자값을 모두 읽어 총합과 평균값을 구한 후 
#평균값을 result.txt라는 파일에 쓰는 프로그램을 작성해보자.

f = open("sample.txt")
lines = f.readlines()
f.close()

total = 0
for line in lines:
	score = int(line)
	total = total + score
	print(total)

average = total/len(lines)
print(average)

f = open("result.txt","w")
f.write(str(average))
f.close()
