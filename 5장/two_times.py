#map(f,iterable) / 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. 
#map은 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수다.
def two_times(numberList):
	result = []
	for number in numberList:
		result.append(number*2)
	return result

result = two_times([1,2,3,4])
print(result)

#위의 예제를 간단하게 바꿔보기
def three_times(x): return x*3
print(list(map(three_times,[1,2,3,4])))

#lambda를 사용하여 간략하게 만들어보기
print(list(map(lambda c: c*2, [1,2,3,4])))
