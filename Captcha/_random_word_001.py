# 영문숫자 난수 20자리 발생
# string.ascii_letters와 string.digits를 함께 사용하고, random.choices() 함수를 통해 랜덤한 문자를 선택

# string.ascii_letters: 영문 대소문자(A-Z, a-z)를 포함합니다.
# string.digits: 숫자(0-9)를 포함합니다.
# random.choices(): characters에서 지정된 길이(length=20)만큼 랜덤하게 문자를 선택합니다.
# ''.join(): 선택된 랜덤 문자들을 하나의 문자열로 결합합니다.

import random
import string

# 영문대소문자,숫자 균일하게 
def generate_random_string(s_type='U', length=20):
    
    # length가 3보다 작으면 최소값 3으로 설정
    if length < 3:
        length = 3
        
     # length를 3개의 변수로 균등하게 나눔
    base_count = length // 3  # 각 타입이 가져갈 기본 개수
    remainder = length % 3    # 나머지 값 (0, 1, 2)
    
    # 각 타입에 기본 개수 할당, 원하는 비율로 대문자, 소문자, 숫자 개수 설정
    num_uppercase = base_count
    num_lowercase = base_count
    num_digits = base_count

    # 나머지를 순차적으로 분배
    if remainder == 1:
        num_uppercase += 1  # 대문자에 하나 더 배분
    elif remainder == 2:
        num_uppercase += 1  # 대문자에 하나 배분
        num_lowercase += 1  # 소문자에 하나 배분 

    # 각 문자 유형에서 원하는 만큼 선택
    uppercase_letters = random.choices(string.ascii_uppercase, k=num_uppercase)
    lowercase_letters = random.choices(string.ascii_lowercase, k=num_lowercase)
    digits = random.choices(string.digits, k=num_digits)

    # 모든 문자들을 합쳐서 무작위로 섞음
    random_string = uppercase_letters + lowercase_letters + digits
    random.shuffle(random_string)
    random_string =  ''.join(random_string)
    
    return random_string


def generate_random_string_old(s_type='U', length=20):
    # string.ascii_uppercase: 영문 대문자 A-Z만을 포함합니다.
    # string.ascii_lowercase: 영문 소문자 a-z만을 포함합니다.
    
    #if s_type == 'U' : # characters = string.ascii_letters + string.digits  # 영문 대소문자 + 숫자
    #    characters = string.ascii_uppercase + string.digits
    #elif s_type == 'L' : # characters = string.ascii_letters + string.digits  # 영문 대소문자 + 숫자
    #    characters = string.ascii_lowercase + string.digits
    #else: # 영문 대소문자와 숫자를 포함한 문자열
    #    characters = string.ascii_letters + string.digits
    
    #print(" s_type = "+ s_type)
    #print(" length = "+ str(length) )
    
    characters = {
        "U": string.ascii_uppercase + string.digits, 
        "L": string.ascii_lowercase + string.digits,
        "A": string.ascii_letters + string.digits       
    }
    
    # 지정한 길이만큼 랜덤하게 문자 선택
    random_string = ''.join(random.choices(characters.get(s_type), k=length))
    
    return random_string

## 함수 호출
#random_string = generate_random_string()
#print(f"랜덤 20자리 영문 숫자 난수: {random_string}")
#random_string = generate_random_string("U",3)
#print(f"랜덤 20자리 영문 숫자 난수: {random_string}")
#random_string = generate_random_string("L",9)
#print(f"랜덤 20자리 영문 숫자 난수: {random_string}")



def switch_demo(day):
    switcher = {
        "A": "월요일",
        2: "화요일",
        3: "수요일",
        4: "목요일",
        5: "금요일",
        6: "토요일",
        7: "일요일"
    }
    return switcher.get(day, "잘못된 입력입니다.")

# 함수 호출
#print(switch_demo("A"))  # 수요일
#print(switch_demo(3))  # 수요일
#print(switch_demo(8))  # 잘못된 입력입니다.

