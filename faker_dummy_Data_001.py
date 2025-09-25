""" pip install Faker
    pip install dummy-data

"""

from faker import Faker

# Faker 객체 생성
fake = Faker('ko_KR') # 'ko_KR'은 한국어 더미 데이터를 생성하도록 설정합니다.

# 기본 정보 더미 데이터 생성
print("--- 기본 정보 ---")
print("이름:", fake.name())
print("주소:", fake.address())
print("전화번호:", fake.phone_number())
print("이메일:", fake.email())
print("회사:", fake.company())
print("직업:", fake.job())
print("생일:", fake.date_of_birth())
print("-" * 20)

# 텍스트 및 문장 더미 데이터
print("--- 텍스트 ---")
print("문장:", fake.sentence())
print("단락:", fake.paragraph())
print("텍스트:", fake.text())
print("-" * 20)

# 숫자 및 날짜/시간 더미 데이터
print("--- 숫자/시간 ---")
print("정수:", fake.random_int(min=1, max=100))
print("날짜:", fake.date_this_year())
print("시간:", fake.time())
print("-" * 20)

# 금융 정보 더미 데이터
print("--- 금융 정보 ---")
print("신용카드 번호:", fake.credit_card_number())
print("통화 코드:", fake.currency_code())
print("-" * 20)

# 한국어(ko_KR)에서만 제공하는 특별한 더미 데이터
print("--- 한국어 특화 ---")
print("주민등록번호:", fake.ssn())
print("우편번호:", fake.postcode())
print("-" * 20)

# 여러 개의 데이터 생성
print("--- 사용자 목록 ---")
for _ in range(3):
    print({
        '이름': fake.name(),
        '이메일': fake.email(),
        '주소': fake.address(),
        '나이': fake.random_int(min=20, max=60),
    })
print("-" * 20)
