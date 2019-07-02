"""
	for문을 배워보자.
for문의 구조
for 변수 in 리스트(또는 튜플, 문자열)
"""

#1. 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
	print(i)

#2. 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first,last) in a:
	print(first + last)
	print("--------------------------")

#for문과 함께 자주 사용하는 range함수
a = range(10)
print(a)

a = range(1,11)
print(a)

#range함수의 예시 살펴보기
sum = 0
for i in range(1,11):
	sum = sum + i
	print(sum)

#리스트 안에 for문 포함하기
a = [1,2,3,4]
result = []
for num in a:
	result.append(num*3)
print(result)

print("-------이것을 더 쉽게 바꿔보자-------")

result2 = [num * 3 for num in a]
print(result2)

#짝수에만 3을 곱하여 담아 보자
result3 = [num * 3 for num in a if num % 2 == 0]
print(result3)

#for문을 2개 이상 사용해서 해보자(복잡함)
result4 = [x*y for x in range(2,10) 
				for y in range(1,10)]
print(result4)

