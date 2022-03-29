
import os
import sys
import konlpy
import pandas as pd
import numpy as np
import re
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
file_name = prePath + "input/NewsResult_19900101-20220216.xlsx" 


# 라이브러리 추가
import numpy as np
import pandas as pd
import re
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 폰트 관련 용도

font_fname = "C:/Windows/Fonts/NanumGothic.ttf"  # A font of your choice
fontprop = fm.FontProperties(fname=font_fname, size=18)
font_name=fm.FontProperties(fname=font_fname).get_name()  #print('-- font_name : ', font_name)
plt.rc('font', family=font_name)

# 깃대종 기사건수
import warnings
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always") 
    df  = pd.read_excel(file_name, sheet_name='sheet', index_col='일자', parse_dates=True, engine="openpyxl")

df1 = df.groupby(df.index.year).size()

# print( df1)
 

# 한나눔 불러오기
from konlpy.tag import Hannanum
hannanum = Hannanum()


# 기사 제목만 별도 텍스트 파일로 저장  
# 엑셀 셀 내용 개행 제거 =SUBSTITUTE(Q2,CHAR(10)," ")
#df[['제목']].to_csv(prePath +'input/bigkinds_title01.txt', index=False, header=False)
#f = open(prePath + 'input/bigkinds_title01.txt','r', encoding='UTF-8')
#lines = f.readlines()
#f.close()

# 기사 본문만 별도 텍스트 파일로 저장 
df[['본문_n']].to_csv(prePath +'input/bigkinds_body_n.csv', index=False, header=False, line_terminator='', encoding='UTF-8-sig' )
f_body = open(prePath + 'input/bigkinds_body_n.csv','r', encoding='UTF-8-sig')
lines = f_body.readlines()
f_body.close()



# 단어 2차원 리스트
dataset = []
for i in range(len(lines)):
    dataset.append(hannanum.nouns(re.sub('[^가-힣a-zA-Z\s]', '', lines[i])))
print(dataset[:10])
  
