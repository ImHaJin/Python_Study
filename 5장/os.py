import os
import glob
import time
#print(os.environ)
print("-----------------------------------------------------")
print(os.environ['PATH'])

#디렉터리 위치 변경하기
print(os.chdir("C:\Windows"))

#디렉터리 위치 리턴받기
print(os.getcwd())

#시스템 명령어 호출하기 
#print(os.system("dir"))

#실행한 시스템 명령어의 결과값 리턴받기 
f = os.popen("dir")
#print(f.read())

#glob.glob("C:/Users/Carl/Desktop/Test")

t = time.time()
t1 = time.localtime(t)
t2 = time.asctime(t1)
t3 = time.ctime()
t4 = time.strftime("UTF-8", t1)
print(t)
print(t1)
print(t2)
print(t3)
print(t4)

