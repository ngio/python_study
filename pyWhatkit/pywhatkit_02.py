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
import pywhatkit as kit

# Replace 'input_image.jpg' with the path to your image file
input_image_path = './python-logo-only.png'

# Replace 'output_ascii_art.txt' with the desired output text file
output_text_file = './python-logo-only'

# Specify the character width (columns) for the ASCII art
#char_width = 100

# Convert image to ASCII art and save to a text file
#kit.image_to_ascii_art(input_image_path, output_text_file, char_width=char_width)
 
# Convert image to ASCII art and save to a text file
kit.image_to_ascii_art(input_image_path, output_text_file)

print(f"ASCII art saved to {output_text_file}")

