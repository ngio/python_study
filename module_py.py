"""
    모듈  Module
"""

# os 모듈의 getcwd 함수를 호출
import os
ret = os.getcwd()
print(ret, type(ret))

# 파일 이름 변경
try:
    os.rename("./before.txt", "./after.txt")
except:
    print("파일이 없어요~")

# 파일 이름 변경
os.rename("./after.txt", "./before.txt")

# numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)
    
 
