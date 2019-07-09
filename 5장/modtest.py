import sys


#파이썬이 설치되어 있는 디렉터리들을 보여준다.
print(sys.path)

sys.path.append("C:\Python_Study\Mymodules")
print(sys.path)

import mod2
print(mod2.sum(3,4))