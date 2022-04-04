import os
import sys
import konlpy
import pandas as pd
import numpy as np
os.environ['JAVA_OPTS'] = 'Xmx4096M'
 
    
## 시간 표시  ##################################### 
import time
import datetime
now = datetime.datetime.now()

timeserise = time.time()
timeserise = str(int(timeserise))
print(timeserise)
print(now)
#################################################  


#작업하는 경로(위치)가 어디인지 확인
print(os.getcwd())

prePath = "./Project/network/"
file_name = prePath + "input/NewsResult_19900101-20220211.xlsx" 


# 라이브러리 추가
import pandas as pd
import re

# 기사 제목만 별도 텍스트 파일로 저장 
f = open(prePath + 'input/bigkinds_title01.txt','r', encoding='UTF-8')
lines = f.readlines()
f.close()

# 한나눔 불러오기
from konlpy.tag import Hannanum
hannanum = Hannanum()

#단어 2차원 리스트
dataset = []
for i in range(len(lines)):
    dataset.append(hannanum.nouns( re.sub('[^가-힣a-zA-Z\s]', '', lines[i] ) ))
#print(dataset[:10])

