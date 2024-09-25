import random
import string

def generate_random_string(length=6):
    # 영문 대문자, 소문자, 숫자를 사용할 수 있는 문자 목록
    characters = string.ascii_letters + string.digits
    
    # 지정한 길이만큼 랜덤하게 문자 선택
    random_string = ''.join(random.choices(characters, k=length))
    
    return random_string 