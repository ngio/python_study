# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 


from PIL import Image
import pytesseract  

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

directory_base = str(real_path)+"./img/"  # 경로object를 문자열로 변경해서 합친다. 

        
# Open an image file
image_path = directory_base+"02.png"  # Replace with your image file path
img = Image.open(image_path)

# Use Tesseract to extract text
text = pytesseract.image_to_string(img)

print("Extracted Text:" + text)



if __name__ == "__main__":
     
    # List all files in the directory
    file_list = [f for f in os.listdir(directory_base) if os.path.isfile(os.path.join(directory_base, f))]

    # Print the list of files
    for file in file_list:
        print(file)
        # Open an image file
        image_path = directory_base + file  # Replace with your image file path
        img = Image.open(image_path)

        text = pytesseract.image_to_string(img)
        print("Extracted Text:")
        print(text)

