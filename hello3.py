#문자열 포매팅 = 문자열은 같으나, 특정한 값을 바꿔야할 때 이것을 가능하게 해주는 것이다.
#여기서 %d는 문자열 포맷코드라고 부른다.
#숫자를 넣기 위해서는 #d, 문자를 넣기 위해서는 #s
print("난 %d 할 수 있다. 내가 최고다" %28)
print("난 %s 할 수 있다. 내가 최고다" %"good")

#숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples" %number)

#2개 이상의 값 넣어보자.
number = 3
strr = "사"
print("조%d모%s" %(number,strr))

print("Error is %d%." %98)