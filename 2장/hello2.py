a = "python"
print(a*2)

print("=" * 50)
print("나는 할 수 있어")
print("=" * 50)

#인덱싱 = 무엇인가를 가리킨다.
#문자열 인덱싱 = 문자열 내 특정한 값을 뽑아내는 것을 말한다.
b = "Life is too short, You need Python"
print(b[3])
print(b[-1])

#문자열 슬라이싱 기법 = 문자를 잘라내는 것을 말한다.
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print(a[0:6])
print(a[1:4])

#시작번호에서 끝 번호부분까지 뽑아낸다.
print(a[1:])
print(a[0:-3])
print(a[19:-5])

#슬라이싱으로 문자열 나누보기
c = "20010331Rainy"
date = c[:8]
weather = c[8:] 
print(date)
print(weather)

#연동/월/일 나눠보기
d = "20010331Rainy"
year = d[0:4]
day = d[4:8]
weather = d[8:]

print(year)
print(day)
print(weather)

#문자열을 바꿔보기
#한 문자만 바꿀 수는 없다. 문자열은 요소값을 바꿀 수 있는 값이 아님 =>immutable한 자료형이라 부름(값을 바꿀 수 없는)
e = "Pithon"
#e[1] = "y"

print(e[:1])
print(e[2:])
print(e[:1] + "y" + e[2:])
