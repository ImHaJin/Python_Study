def positive(numberList):
	result = []
	for num in numberList:
		if num > 0:
			result.append(num)

	return result

print(positive([2,20,-20]))

def positive1(a):
	return a > 0

#filter()를 이용해서 간단하게 작성하기
print(list(filter(positive1, [1,2,3,4,-1,-2,-3,-4])))		

#lambda로 더욱 편하게 코드 작성하기
print(list(filter(lambda x: x>0, [5,6,-5,-6])))

