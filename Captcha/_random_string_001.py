# 영문숫자 난수 20자리 발생
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
