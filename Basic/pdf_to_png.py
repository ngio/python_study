# PyMuPDF
# pip install PyMuPDF 

import fitz  # PyMuPDF


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

directory_base = str(real_path)+"./ONE/"  # 경로object를 문자열로 변경해서 합친다. 
 


def pdf_to_png(pdf_file, input_pdf_name, output_folder, dpi = 300):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)
    
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]
        
        # Convert the page to an image
        # image = page.get_pixmap()
        image = page.get_pixmap(dpi = dpi)
        
        # Save the image as a PNG file
        image.save(f"{output_folder}/{input_pdf_name}_{page_number + 1}.png", "png")

    # Close the PDF file
    pdf_document.close()

if __name__ == "__main__":
     
    # List all files in the directory
    file_list = [f for f in os.listdir(directory_base) if os.path.isfile(os.path.join(directory_base, f))]

    # Print the list of files
    for file in file_list:
        print(file)
        
        #input_pdf = "./TWO/"+ file_name +".pdf"  # Replace with your PDF file path
        input_pdf      = "./ONE/"+ file  # Replace with your PDF file path
        input_pdf_name = os.path.splitext(file)[0]
        print(input_pdf_name)
        output_folder  = "./ONE/data"  # Replace with your output folder
        dpi = 600
     
        pdf_to_png(input_pdf, input_pdf_name, output_folder, dpi)
   
