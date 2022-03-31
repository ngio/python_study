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
plt.show()

# 국립공원이 언급된 깃대종 기사건수
df2 = df[df['제목'].str.contains('국립공원') | df['본문'].str.contains('국립공원')]
df2 = df2.groupby(df2.index.year).size()
f, ax = plt.subplots(figsize=(16, 8)); plt.xticks(df2.index, rotation=90)
plot = ax.bar(df2.index, df2.values)
for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2. , height, '%d' %int(height), ha='center' , va='bottom' )

plt.title('깃대종 뉴스 내 국립공원이 언급된 기사 빈도수')
plt.savefig(prePath +'output/img02.png', bbox_inches='tight')    

# 깃대종 기사 건수와 국립공원이 언급된 깃대종 기사 건수를 비교한 바 플롯입니다.
pd.concat([df1,df2], axis=1).plot(kind='bar', figsize=(16,8))
plt.legend(["깃대종 기사 건수", "국립공원이 언급된 깃대종 기사 건수"])
plt.savefig(prePath +'output/img03.png', bbox_inches='tight')

# 기사 건수로 보면 깃대종 기사 1,029건 중 국립공원이 언급된 기사는 380건, 36.9%를 차지합니다.
print('깃대종 기사 '+ str(df1.sum()) + '건 중 국립공원이 언급된 깃대종 기사 '+ str(df2.sum()) + ' 건 : ' + str(format(df2.sum() / df1.sum() * 100, ".1f") + '% 차지') )


# 한나눔 불러오기
from konlpy.tag import Hannanum
hannanum = Hannanum()

# 기사 제목만 별도 텍스트 파일로 저장
df[['제목']].to_csv(prePath +'input/bigkinds_title01.txt', index=False, header=False)
f = open(prePath + 'input/bigkinds_title01.txt','r', encoding='UTF-8')
lines = f.readlines()
f.close()

# 단어빈도 분석 - 상위 20개 단어
words = []
for i in range(len(lines)):
    nouns  = hannanum.nouns(lines[i])  # 명사 분석        
    """
    morphs = hannanum.morphs(lines[i]) # 문장 분석
    pos    = hannanum.pos(lines[i])    # 형태소 분석  
    """   
    for n in nouns:          #nonus 가 단어 배열이어서 한번 더 나누어서 word에 추가
        if len(n)>1:         # 명사중에 길이가 1 이상인것만 추가
            words.append(n)
    
def flatten(l):
    flatList = []
    for elem in l:
        if type(elem) == list:
            for e in elem:
                flatList.append(elem)
        else:
            flatList.append(elem)
    return flatList

word_list = flatten(words)
word_list = pd.Series([x for x in word_list if len(x)>1 ])
word_list.value_counts().head(20)
print("# 단어빈도 분석 : 상위 20")
print(word_list.value_counts().head(20))

# WordCloud =========================================

from wordcloud import WordCloud
from collections import Counter

count = Counter(word_list)
max_words_num = 100

font_name=fm.FontProperties(fname="C:\\Windows\\Fonts\\NanumGothic.ttf").get_name()
rc('font', family=font_name)
wordcloud = WordCloud(
    font_path = 'C:\\Windows\\Fonts\\NanumGothic.ttf'    # 맥에선 한글폰트 설정 잘해야함.
    , background_color='white'                             # 배경 색깔 정하기
    #, colormap = 'Accent_r'                                # 폰트 색깔 정하기
    , width = 800
    , height = 800
    , max_words=max_words_num
    , max_font_size=300
    #, mask=r2d2_mask
    #, stopwords=stopwords
).generate_from_frequencies(count)
array = wordcloud.to_array()        

fig = plt.figure(figsize=(10,10))
plt.imshow(array, interpolation='bilinear')
plt.axis('off')
plt.savefig(prePath +'output/img04.png', bbox_inches='tight')



# WordCloud ========== 깃대종 제외한 클라우드 ===============================
count.pop('깃대종')
wordcloud = wordcloud.generate_from_frequencies(count)
array = wordcloud.to_array()

fig = plt.figure(figsize=(10,10))
plt.imshow(array, interpolation="bilinear")
plt.axis('off')
plt.savefig(prePath +'output/img05.png', bbox_inches='tight')
plt.show()
