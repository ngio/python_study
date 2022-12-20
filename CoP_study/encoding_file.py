""" 
    인코딩 정보
    파일 인코딩 관련
    file encoding 
    UTF-8  
    UTF-8-SIG
"""
import os
import sys 
 
#작업하는 경로(위치)가 어디인지 확인
#print(os.getcwd())
prePath_in = "./Project/" 
prePath_out = "./Project/" 



#1. 기본 내용적기

# 기본 텍스트 신규 입력
file = open("test.txt", "w")
file.write("내용입력")
file.close()

# 한글깨짐 방지 ENCODING UTF-8
file = open("test.txt", "w", encoding="UTF-8")
file.write("내용입력")
file.close()

# 한글깨짐 방지2 ENCODING UTF-8
# txt는 UTF-8로도 충분한데 csv는 UTF-8로만 하면 읽을땐 다른걸로 읽을 경우 깨짐 현상 발생
file = open("test.csv", "w", encoding="UTF-8-sig")
file.write("test,test,test\n")
file.write("잘되나,안된다,오된다\n")
file.close()

# 참고
# Permission denied: 'test.csv' 가 나온다
# 파일 열고 있어서 수정할 수 없다는거다. 꺼주자.

# 추가 입력
file = open("test.txt", "a")
file.write("추가 내용입력")
file.close()


# 읽기
file = open("test.txt", "r", encoding="UTF-8")
print(file.read())
file.close()

# with 함수 : open & close 포함 
with open("test.txt", "w", encoding="UTF-8") as file:
    file.write("내용입력")
with open("test.txt", "r", encoding="UTF-8") as file:
    print(file.read())
 

 

#2. print 한거 txt 파일에 넣기

# sys.stdout 함수 사용하여 log 저장하기
f = open('test.txt','w', encoding='utf-8') # 로그 저장할 file open
sys.stdout = f
print("내용입력")
sys.stdout = sys.__stdout__   # 원래의 stdout으로 복구
f.close()                     # 로그 파일 닫기

#이렇게 해도 되긴 하는데.. 프로그램이 종료 안되면 문제가 생길듯?
sys.stdout = open('test.txt','w', encoding='utf-8')
print("내용입력")
