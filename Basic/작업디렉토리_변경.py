

# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os

#현재 폴더 경로; 작업 폴더 기준
print(os.getcwd())

#현재 파일의 폴더 경로; 작업 파일 기준
real_path = os.path.dirname(os.path.realpath(__file__))
print(real_path)

#작업 디렉토리 변경
os.chdir(real_path)

