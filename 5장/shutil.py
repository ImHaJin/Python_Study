import shutil

#src라는 이름의 파일을 dst로 복사한다.
#만약 dst가 디렉터리 이름이라면, src라는 파일 이름으로 dst라는 dst디렉터리에 복사한다. 동일한 파일 이름이 있을 경우 덮어쓴다.
shutil.copy("src.txt", "dst.txt")

