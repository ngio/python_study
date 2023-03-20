"""
    모듈  Module
"""

# os 모듈의 getcwd 함수를 호출
import os
ret = os.getcwd()
print(ret, type(ret))


# 파일 이름 변경
os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")
