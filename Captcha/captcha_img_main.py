# pip install captcha


import random
import string
import os
from captcha.image import ImageCaptcha  # ImageCaptcha 라이브러리를 사용해야 합니다.


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
    characters = string.ascii_letters + string.digits  # 영문 대소문자 + 숫자
    # string.ascii_uppercase: 영문 대문자 A-Z만을 포함합니다.
    # string.ascii_lowercase: 영문 소문자 a-z만을 포함합니다.
    return ''.join(random.choices(characters, k=length))

# 중복되지 않는 파일명 생성 함수
def get_unique_filename(base_name, extension, directory="./img/"):
    counter = 1
    new_filename = f"{base_name}.{extension}"
    
    # 경로 내 파일명이 중복되면 새로운 파일명 생성
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base_name}_{counter}.{extension}"
        counter += 1
    
    return new_filename

# 메인 로직
def main():
    # 캡차 이미지 생성기 설정
    image = ImageCaptcha(width=280, height=90)

    # 랜덤 6자리 문자열 생성
    captcha_text = generate_random_string()
    print(f"\n랜덤 6자리 문자열: {captcha_text}")

    # 이미지 생성
    data = image.generate(captcha_text)

    # 이미지 저장 경로 지정
    img_directory = "./img/"
    os.makedirs(img_directory, exist_ok=True)  # img 폴더가 없을 경우 생성

    # 중복되지 않는 파일명 생성
    unique_filename = get_unique_filename(captcha_text, 'png', directory=img_directory)

    # 이미지 파일 저장
    image.write(captcha_text, os.path.join(img_directory, unique_filename))

    print(f"이미지가 {unique_filename}으로 저장되었습니다.")

# 프로그램 실행
if __name__ == "__main__":
    main()
    
    
    