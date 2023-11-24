# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

#-----------------------------------------------------
from PIL import Image
from io import BytesIO
from art import *
import pywhatkit as kit

# Replace 'input_image.jpg' with the path to your image file 
input_image_path = './python-logo-only.png'

# Replace 'output_ascii_art.txt' with the desired output text file 
output_text_file = './python-logo-only'



# Resize the image to the desired width
width = 100  # Adjust the width as needed
img = Image.open(input_image_path)
aspect_ratio = img.size[1] / float(img.size[0])
height = int(width * aspect_ratio)
img = img.resize((width, height), Image.ANTIALIAS)

# Convert image to ASCII art using art library

# ascii_art_text = text2art(img)
ascii_art = text2art(img.convert("L").tobytes().decode("utf-8"), "block")

# Save ASCII art to a text file
with open(output_text_file, 'w') as file:
    file.write(ascii_art_text)

print(f"ASCII art saved to {output_text_file}")