# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent

print(real_path) # 현재 경로와 같은지 확인하시오. 

#작업 디렉토리 변경
os.chdir(real_path) 

"""_summary_
    1. ./input/에 pdf 파일을 복사해둔다. 
    2. pdf 파일의 이름에 공백이 있으면 공백을 제거
    3. ./output/에 동일이름의 txt 파일을 생성
    4. 생성된 txt 파일의 단어 빈도수 추출 xls 
    5. 끝
"""

import PyPDF2
# pip install PyPDF2

import pandas as pd
from collections import Counter
import re

def extract_text_from_pdf(pdf_path):
    # PDF 파일을 바이너리 읽기 모드로 열기
    with open(pdf_path, "rb") as file:
        # PDF Reader 객체 생성
        pdf_reader = PyPDF2.PdfReader(file)
        
        # 모든 페이지의 텍스트 추출
        text = []
        for page in pdf_reader.pages:
            text.append(page.extract_text())
        
        # 모든 텍스트를 하나의 문자열로 결합
        full_text = "\n".join(text)
    
    return full_text

def save_text_to_txt(text, output_path):
    # 추출된 텍스트를 TXT 파일로 저장
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)
        

def read_text_file(file_path):
    """텍스트 파일을 읽고 내용을 반환"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_word_frequencies(text):
    """주어진 텍스트에서 단어 빈도수 계산"""
    # 소문자 변환 및 정규 표현식을 사용하여 단어 추출
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def save_frequencies_to_excel(frequencies, output_file):
    """단어 빈도수를 엑셀 파일로 저장"""
    # 판다스 DataFrame으로 변환
    df = pd.DataFrame(list(frequencies.items()), columns=['Word', 'Frequency'])
     # 빈도수 내림차순, 단어 알파벳순 오름차순으로 정렬
    df = df.sort_values(by=['Frequency', 'Word'], ascending=[False, True])
    # 데이터를 엑셀 파일로 저장
    df.to_excel(output_file, index=False)


  
  
  
directory_base = str(real_path)+"/input/"  # 경로object를 문자열로 변경해서 합친다. 

if __name__ == "__main__":
     
    # List all files in the directory
    file_list = [f for f in os.listdir(directory_base) if os.path.isfile(os.path.join(directory_base, f))]
             
    # Print the list of files
    for file  in os.listdir(directory_base):
        old_file = os.path.join(directory_base, file)
        new_file_name = file.replace(" ","_")
        new_file = os.path.join(directory_base, new_file_name) # 파일명에서 공백을 언더바로 치환
        os.rename(old_file, new_file)        
        
        txt_output_path = "./output/"+ new_file_name +"_.txt"
        
        # PDF에서 텍스트 추출
        extracted_text = extract_text_from_pdf(new_file)
        # 텍스트를 TXT 파일로 저장
        save_text_to_txt(extracted_text, txt_output_path)
         
        print(txt_output_path)


        # 파일 읽기
        text = read_text_file(txt_output_path)

        # 빈도수 분석
        frequencies = count_word_frequencies(text)

        # 엑셀로 저장
        output_excel = "./output/"+ new_file_name +"_word_frequencies.xlsx"
        save_frequencies_to_excel(frequencies, output_excel)

    
    print("단어 빈도수가 엑셀 파일로 저장되었습니다.")
    
    