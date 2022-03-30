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
file_name = prePath + "input/NewsResult_19900101-20220216.xlsx" 

# 라이브러리 추가
import pandas as pd
import seaborn as sns
sns.set(style='darkgrid',font='KoPubDotum', font_scale=1.5 )
from matplotlib import rc
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

f, ax = plt.subplots(figsize=(16,8))     # nrows=2, ncols=1, index=2
plt.xticks(df1.index, rotation=90)

plot = ax.bar(df1.index, df1.values)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() * rect.get_width()/2, height, '%d' %int(height), ha='center', va='bottom')

plt.title('깃대종 뉴스 빈도수')
plt.xlabel('x 좌표')
plt.ylabel('y 좌표')

#fig1 = plt.gcf()
#fig1.savefig(prePath +'img01.png' )
plt.savefig(prePath +'output/img01.png' )
#plt.show()
