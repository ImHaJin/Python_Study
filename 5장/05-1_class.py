result = 0
def adder(num):
	global result
	result += num
	return result

print(adder(3))
print(adder(4))

class Calculator:
	def __init__(self):
		self.result = 0
	
	def adder(self,num):
		self.result += num
		return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

