'''
	리스트 관련 함수들
자주 사용되는 리스트 함수들을 알아보자
'''

#리스트에 요소 추가(append)
a = [1,2,3]
a.append(4)
print(a)

#리스트에 리스트 추가
a.append([5,6])
print(a)

#리스트 정렬(sort)
a = [1,4,2,3]
a.sort()
print(a)

a = ['b','c','d']
a.sort()
print(a)

#리스트 뒤집기(reverse)
a = ['c','d','f']
a.reverse()
print(a)

#위치반환(index)
a = [1,2,3]
print(a.index(3))
print(a.index(1))

#리스트에 요소 삽입(insert)
a = [1,2,3]
a.insert(0,4)
print(a)
a.insert(2,5)
print(a)

#리스트 요소 제거(remove)
a = [1,2,3,4,5,6,3]
a.remove(3)
print(a)
a.remove(3)
print(a)

#리스트 요소 끄집어내기(pop)
a = [1,2,3]
a.pop() #맨 마지막 요소를 돌려주고 그 요소는 삭제하는 함수이다.
print(a)

a = ['1','2','3']
a.pop(1) #pop(x)는 x번째 요소를 돌려 주고 그 요소는 삭제한다.
print(a)

#리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,1]
print(a.count(1))

#리스트 확장(extend) / extend(x)에서 x는 리스트만 올 수 있으며 원래의 a리스트에 x리스트를 더하게 된다.
a = [1,2,3]
a.extend([4,5])
print(a)


