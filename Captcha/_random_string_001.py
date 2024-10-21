# 영문숫자 난수 20자리 발생
# string.ascii_letters와 string.digits를 함께 사용하고, random.choices() 함수를 통해 랜덤한 문자를 선택

# string.ascii_letters: 영문 대소문자(A-Z, a-z)를 포함합니다.
# string.digits: 숫자(0-9)를 포함합니다.
# random.choices(): characters에서 지정된 길이(length=20)만큼 랜덤하게 문자를 선택합니다.
# ''.join(): 선택된 랜덤 문자들을 하나의 문자열로 결합합니다.

import random
import string

def generate_random_string(length=20):
    # 영문 대소문자와 숫자를 포함한 문자열
    characters = string.ascii_letters + string.digits
    
    # 지정한 길이만큼 랜덤하게 문자 선택
    random_string = ''.join(random.choices(characters, k=length))
    
    return random_string

# 함수 호출
random_string = generate_random_string()
print(f"랜덤 20자리 영문 숫자 난수: {random_string}")
