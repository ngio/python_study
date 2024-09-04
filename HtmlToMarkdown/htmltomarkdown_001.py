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
 * 사용 방법
    1.HTML 파일 경로(html_file_path)와 변환된 Markdown 파일을 저장할 경로(output_md_file_path)를 지정합니다.
    2.코드를 실행하면 HTML 파일에 포함된 테이블을 포함한 모든 내용을 Markdown 형식으로 변환하여 저장합니다.
"""


from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os

def convert_html_table_to_md(html_file_path, output_md_file_path):
    # HTML 파일 읽기
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(html_content, 'html.parser')

    # HTML을 Markdown으로 변환
    markdown_content = md(str(soup))

    # 결과를 Markdown 파일로 저장
    with open(output_md_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    
    print(f"Converted HTML table to Markdown and saved as: {output_md_file_path}")

# 사용 예시
#html_file_path = 'path_to_your_html_file.html'  # 변환할 HTML 파일 경로
html_file_path = 'test_001.html'  # 변환할 HTML 파일 경로
output_md_file_path = 'output_markdown_file.md'  # 저장할 Markdown 파일 경로

convert_html_table_to_md(html_file_path, output_md_file_path)

