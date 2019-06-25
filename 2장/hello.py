#hello.py
print("Hello")

a = 2+3j
print(a.real)

b = 1+4j
print(b.imag)

c = 3+2j
print(c.conjugate())

d = 1+2j
print(abs(d))

a = 6
b = 3
print(a**b)

a = 11
b = 3 
print(a%b)

a = 13 
b = 3 
print(a/b)

a = 13 
b = 3 
print(a//b)

food = "맛있는's 음식이 먹고 싶다"
print(food)

coffee = '"맛있는 커피가" \'마시고\' 싶어'
print(coffee)

multiLine = "한화시스템 계약이 잘되었으면 좋겠다. \n인센티브 가즈아아!!!"
print(multiLine)

manyLine = '''
많은 글
많은 글재주
많은 글쓰기
'''
print(manyLine)


manyLine2 = """
많은 글
많은 글재주
많은 글쓰기
"""
print(manyLine2)

head = "머리"
body = "몸"

print(head + body*2)