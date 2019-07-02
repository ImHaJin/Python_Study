#for문과 continue
marks = [90,80,70,60,50,40]
number = 0
for mark in marks: 
	number = number + 1
	if mark < 60: continue
	print("%d번 학생 축하합니다. 합격입니다" %number)