# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

"""_summary_
pip install pillow
pip install pytesseract



다운 받아야하는 학습된 한글 데이터 파일명: kor.traineddata
파일 위치: tesseract가 설치된 경로 C:\Program Files\Tesseract-OCR\tessdata

"""

from PIL import Image
import pytesseract  
import cv2 
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Tesseract의 tessdata 경로를 수동으로 지정해야 할 때 설정
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

#config = ('-l kor_vert --oem 3 --psm 11') #한글이 세로로 있을때
#config = ('-l kor+eng --oem 3 --psm 11')  #  텍스트가 흩어져 있는 이미지에 적합합니다.
#config = ('-l kor+eng --oem 3 --psm 6')
config = ('-l kor+eng --oem 3 --psm 4')
#config = ('-l kor+eng --oem 3 --psm 3')
#config = ('-l kor+eng')
directory_base = str(real_path)+"./img/50/"  # 경로object를 문자열로 변경해서 합친다. 

        
"""
    # Open an image file
    image_path = directory_base+"03_kor_eng.png"  # Replace with your image file path
    img = Image.open(image_path)


    # Use Tesseract to extract text
    text = pytesseract.image_to_string(img, config=config)

    print("Extracted Text:" + text)

    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(rgb_image)

    # use Tesseract to OCR the image 
    # text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
    text = pytesseract.image_to_string(rgb_image, config=config)
    print(text)
"""

if __name__ == "__main__":
     
    # List all files in the directory
    file_list = [f for f in os.listdir(directory_base) if os.path.isfile(os.path.join(directory_base, f))]

    # Print the list of files
    for file in file_list:
        print(file)
        # Open an image file
        image_path = directory_base + file  # Replace with your image file path
        img = Image.open(image_path)

        text = pytesseract.image_to_string(img, config=config) 
        print("Extracted Text:")
        print(text)
        
        output_md_file_path = 'output_img_to_Text_file.txt'  # 저장할 Markdown 파일 경로
        # 결과를 Markdown 파일로 저장
        #with open(output_md_file_path, 'w', encoding='utf-8') as file:
        with open(output_md_file_path, 'a', encoding='utf-8') as file:   # a : 내용이 있으면 이어서 쓴다.
            file.write(text)
        
    
    print(f"Converted HTML table to Markdown and saved as: {output_md_file_path}")

