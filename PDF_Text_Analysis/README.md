
## PDF_Text_Analysis

PDF 파일을 읽어서 text 파일로 저장한 후  단어 빈도수를 엑셀로 저장한다. 

인식되지 않는 단어가 있다면 인식가능하게 해야할 필요가 있다. 

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

