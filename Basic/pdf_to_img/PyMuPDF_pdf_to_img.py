# PyMuPDF로 코딩 없이 PDF에서 이미지 추출


# PyMuPDF


# pip install PyMuPDF



import fitz
doc = fitz.open(PDF_FILE_PATH)
for i, page in enumerate(doc):
    img = page.get_pixmap()
    img.save(f"./data/{i}.png")



# Command 로 바로 실행하기 
# python -m fitz extract -images input.pdf
