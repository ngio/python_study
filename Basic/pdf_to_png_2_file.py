# python one file pdf to png, Increase resolution

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



def pdf_to_png(pdf_file, output_folder, dpi=300):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)
    
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]
        
        # Set the resolution (DPI)
        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)
        image = page.get_pixmap(matrix=mat)
        
        # Save the image as a PNG file
        image.save(f"{output_folder}/page_{page_number + 1}.png", "png")

    # Close the PDF file
    pdf_document.close()

if __name__ == "__main__":
    input_pdf = "Guam_0820.pdf"  # Replace with your PDF file path
    output_folder = "output_images"  # Replace with your output folder
    dpi = 600  # Adjust DPI as needed
    
    pdf_to_png(input_pdf, output_folder, dpi)
