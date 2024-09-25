# pip install captcha


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


# Import the following modules
from captcha.image import ImageCaptcha


"""
주어진 파일명과 확장자를 바탕으로 파일이 중복되지 않는 고유 파일명을 반환하는 함수
"""
def get_unique_filename(base_name, extension):
    
    counter = 1
    new_filename = f"{base_name}.{extension}"
    
    # 파일명이 중복될 경우 새로운 파일명을 생성
    while os.path.exists(new_filename):
        new_filename = f"{base_name}_{counter}.{extension}"
        counter += 1
    
    return new_filename


# Create an image instance of the given size
image = ImageCaptcha(width = 280, height = 90)

# Image captcha text
captcha_text = 'GeeksforGeeks'

# generate the image of the given text
data = image.generate(captcha_text) 

# write the image on the given file and save it
#image.write(captcha_text, 'CAPTCHA.png')
 
# 파일명을 중복되지 않도록 생성
unique_filename = get_unique_filename(captcha_text, 'png')

# 이미지 파일을 저장
image.write(captcha_text, unique_filename)

print(f"이미지가 {unique_filename}으로 저장되었습니다.")



