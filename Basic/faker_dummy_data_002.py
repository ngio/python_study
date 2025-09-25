""" pip install Faker
    
    1.faker는 이름, 주소, 이메일, 전화번호 등 다양한 종류의 가짜 데이터를 만들어주는 파이썬 패키지입니다. 
       Faker 객체를 생성하고, 해당 객체가 제공하는 다양한 메소드를 호출해 원하는 형식의 데이터를 얻을 수 있어요.
    2.Faker는 국가별 언어 설정을 지원해요. 예를 들어, Faker('ko_KR')를 사용하면 한국어 이름, 주소, 주민등록번호 등 한국 특화된 데이터를 생성할 수 있습니다.
    
    * Faker에 커스텀 전화번호 Provider 추가
    

How to Create Sample Data With Python and Faker
참고 영상 : youtube.com/watch?reload=9&v=u2QQOOKFoww
    
* 프로그램의 기능
    1.더미 데이터 생성: Faker의 name(), address(), email() 등 다양한 메소드를 호출하여 데이터를 만듭니다. Faker('ko_KR')를 사용하면 한국어 데이터가 생성되어 더 현실적입니다.
    2.구조화된 데이터: 생성된 데이터를 딕셔너리 형태로 저장하고, 이를 pd.DataFrame()을 이용해 테이블 형태로 변환합니다.
    3.파일 저장: df.to_csv() 메소드를 사용해 데이터를 CSV 파일로 저장합니다. index=False는 DataFrame의 인덱스를 파일에 포함하지 않도록 합니다. encoding='utf-8-sig'는 한글 깨짐을 방지하는 인코딩 방식입니다.

"""
# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 


#==============================================================

# 더미 데이터 생성을 위한 faker와 pandas 라이브러리 불러오기
from faker import Faker
import pandas as pd
import os
import random


# Faker에서 Base Provider를 임포트
from faker.providers.phone_number.ko_KR import Provider as PhoneNumberProvider

# 커스텀 Provider 클래스 정의
class MyCustomPhoneNumberProvider(PhoneNumberProvider):
    # phone_number 메소드 오버라이드
    def phone_number(self):
        # 010으로 시작하는 번호 생성
        #return '010-' + self.numerify('####-####')
        return '019-' + self.numerify('####-####')

#==============================================================

# Faker 객체 생성 (한국어 데이터 설정)
fake = Faker('ko_KR')
# 커스텀 Provider 추가
fake.add_provider(MyCustomPhoneNumberProvider)

# 사용자 데이터를 담을 리스트
user_data = []

# 생성할 사용자 데이터 수
NUM_USERS = 100

print(f"{NUM_USERS}명의 더미 사용자 데이터를 생성합니다...")

# 반복문을 이용해 데이터 생성
for i in range(NUM_USERS):
    # Faker를 이용해 사용자 정보 생성
    user_info = {
        'ID': i + 1,
        '이름': fake.name(),
        '주소': fake.address(),
        '이메일': fake.email(),
        '전화번호': fake.phone_number(),
        '회사': fake.company(),
        '직업': fake.job(),
        '생년월일': fake.date_of_birth(minimum_age=20, maximum_age=60),
        '주민등록번호': fake.ssn()
    }
    user_data.append(user_info)
    
print("데이터 생성이 완료되었습니다.")

# 데이터프레임으로 변환
df = pd.DataFrame(user_data)

print(df)

# CSV 파일로 저장
file_name = 'dummy_users.csv'
df.to_csv(file_name, index=False, encoding='utf-8-sig')

print(f"데이터가 '{os.getcwd()}' 폴더의 '{file_name}' 파일로 저장되었습니다.")
