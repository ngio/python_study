"""   
랜덤으로 생성된 문자열을 엑셀 파일에 저장
"""
import random
import string
import os
from captcha.image import ImageCaptcha
import pandas as pd  # pandas 라이브러리를 사용하여 엑셀 파일 저장

# 2023-05-26 ngio add
# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 


# 랜덤 6자리 문자열 생성 함수
def generate_random_string(length=6):
    # string.ascii_uppercase: 영문 대문자 A-Z만을 포함합니다.
    # string.ascii_lowercase: 영문 소문자 a-z만을 포함합니다.
    # characters = string.ascii_letters + string.digits  # 영문 대소문자 + 숫자
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length)) 

# 초기 데이터
data = [['QWE123', 10001], ['RTY456', 10002]]

# 반복문을 통해 데이터 추가
for i in range(1, 10):
    #letter = chr(64 + i)  # A: 65 -> B: 66 -> C: 67 -> ...
    letter = generate_random_string();
    data.append([letter, (10002 + i)])

print(data)
print("\n\n")

# 중복 값 확인 함수
def check_duplicates(data):
    # 리스트를 튜플로 변환 (리스트는 set에 직접 넣을 수 없기 때문)
    data_as_tuples = [tuple(item) for item in data]
    
    # 집합의 크기와 리스트의 크기를 비교
    if len(data_as_tuples) != len(set(data_as_tuples)):
        print("중복된 값이 있습니다.")
    else:
        print("중복된 값이 없습니다.")

# 함수 호출
check_duplicates(data)
print("\n\n")


# DataFrame으로 변환
df = pd.DataFrame(data, columns=['random_word', 'word_index'])

# 결과 출력
print(df)
print("\n\n")