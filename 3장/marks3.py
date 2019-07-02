marks = [90,80,70,60,50,40]
for number in range(len(marks)):
	if marks[number] < 60: continue
	print("%d번 학생 축하합니다. 합격입니다." %(number+1))
