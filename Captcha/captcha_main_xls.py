"""   
랜덤으로 생성된 문자열을 이미지 파일로 저장한 후, 해당 문자열을 엑셀 파일에 저장
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
    characters = string.ascii_letters + string.digits  # 영문 대소문자 + 숫자
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

# 문자열을 엑셀 파일에 저장하는 함수
def save_string_to_excel(random_string, excel_file="captcha_strings.xlsx"):
    # 데이터프레임으로 변환 (열 이름은 "Captcha Text")
    df = pd.DataFrame([random_string], columns=["Captcha Text"])

    # 엑셀 파일이 이미 있으면 기존 파일에 추가, 없으면 새로 생성
    if os.path.exists(excel_file):
        existing_df = pd.read_excel(excel_file)
        df = pd.concat([existing_df, df], ignore_index=True)
    
    # 엑셀 파일 저장
    df.to_excel(excel_file, index=False)
    print(f"'{random_string}' 문자열이 {excel_file}에 저장되었습니다.")

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

    # 생성된 문자열을 엑셀에 저장
    save_string_to_excel(captcha_text)

# 프로그램 실행
if __name__ == "__main__":
    main()