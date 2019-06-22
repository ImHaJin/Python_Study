#문자열 관련 함수들

#문자 개수 세기(문자 b의 개수를 반환)
a = "hobby"
print(a.count('b'))

'''
위치 알려주기1(find)
b가 처음으로 나온 위치 알려주기 / 만약 찾는 문자나 문자열이 존재하지 않는다면 -1
'''
b = "Python is best choice"
print(b.find('P'))

'''
위치 알려주기2(index)
문자열 중 o가 맨 처음으로 나온 위치를 반환한다. 
find함수와 다른 점은 문자열 안에 존재하지 않은 문자를 찾으면 오류가 발생한다.
'''
c = "Life is too short"
print(c.index("o"))

'''
문자열 삽입(join)
'''
d = "."
print(d.join("임하진"))


#소문자를 대문자로 바꾸기(upper)
e = "hi"
print(e.upper())

#대문자를 소문자로 바꾸기(lower)
f = "Hi"
print(f.lower())

#왼쪽 공백 지우기(lstrip)
g = " hi "
print(g.lstrip())

#오른쪽 공백 지우기(rstrip)
h = " hi "

#양쪽 공백 지우기(strip)
i = " hi "
print(i.strip())

#문자열 바꾸기(replace)
j = "have delicious food"
print(j.replace("food", "icecream"))

'''
문자열 나누기(split)
k.split()처럼 괄호 안에 아무런 값도 넣어 주지 않으면 공백을 기준으로 문자열을 나눠준다.
'''
k = "have delicious food"
print(k.split())

l = "a:b:c:d:e"
print(l.split(":"))

