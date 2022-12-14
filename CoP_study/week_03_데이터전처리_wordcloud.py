"""텍스트 분석 5단계
1. 데이터 수집 
2. 데이터 전처리 : 데이터를 다루기 편하게 만들어 놓기 위한 준비 단계
3. 데이터 탐색 
4. 데이터 분석
5. 인사이트 추출
"""
import konlpy
import pandas as pd
import numpy as np
import os
os.environ['JAVA_OPTS'] = 'Xmx4096M'
os.getcwd()  # 현재 디렉토리 경로 확인 , 작업하는 경로(위치)가 어디인지 확인

""" 
형태소 분석 및 품사 태깅 : https://konlpy.org/ko/latest/morph/
  형태소 분석 이란 형태소를 비롯하여, 어근, 접두사/접미사, 품사(POS, part-of-speech) 등 다양한 언어적 속성의 구조를 파악하는 것입니다.
  품사 태깅 은 형태소의 뜻과 문맥을 고려하여 그것에 마크업을 하는 일입니다. 예를 들어:

"""
### Okt Class : https://konlpy.org/ko/latest/api/konlpy.tag/#konlpy.tag._hannanum.Hannanum 
from konlpy.tag import Okt
 
file = open("D:\\python\\jupyter_data\\notebook\\data_0.txt", "rt", encoding="utf-8-sig")
lines = file.readlines()
 
file.close()
#print(lines)
twitter = Okt()
sentences_tag = []
 
for sentence in lines:
    sentences_tag.append(twitter.pos(sentence))
    
print(sentences_tag) #""" 첫번째 원소가 낱말, 두번째 원소가 형태소 """





noun_adj_list=[]
 
for sentence in sentences_tag :
    for word, tag in sentence :  #"""첫번째 원소를 word로, 두번째 원소를 tag로 할당"""
        if tag in ['Noun', 'Adjective'] : #""" tag가 Noun, Adjective 중 하나라면 word를 noun_adj_list에 적재 """
            noun_adj_list.append(word)

# 추출된 명사 리시트 저장            
with open('data_0_list.txt','w',encoding='UTF-8') as f:
    for name in noun_adj_list:
        f.write(name+'\n')            
f.close()

print(noun_adj_list)




# 패키지 로딩하기
from matplotlib import rc
import matplotlib.pyplot as plt
"""
   IPython 에서 제공하는 Rich output.  
   도표와 같은 그림, 소리, 애니메이션 과 같은 결과물들을 Rich output
   notebook을 실행한 브라우저에서 바로 그림을 볼 수 있게 해주는 것 
"""
%matplotlib inline    


from wordcloud import WordCloud
from collections import Counter

import re


#저장된 리스트에서 다시 불러오기
file = open("D:\\python\\jupyter_data\\notebook\\data_0_list.txt", "rt", encoding="utf-8-sig")
lines = file.readlines()
file.close()

noun_adj_list = []
 
for sentence in lines:    
    sentence = re.sub("\n", "", sentence)
    sentence = sentence.strip()
    # print(len(sentence), sentence)
    if(  len(sentence) > 1 ):
        noun_adj_list.append(sentence)
    if( sentence == "삶"  ):
        noun_adj_list.append(sentence)

# print(noun_adj_list)
# type(noun_adj_list)

count = Counter(noun_adj_list)
words = dict(count.most_common())
#words = dict(count.most_common(50))  # 가장 많은 것 중 50개를 가져와라

words




from wordcloud import WordCloud 
import matplotlib.font_manager as fm  # 폰트 관련 용도

# dict 
max_words_num = 200

font_name=fm.FontProperties(fname="C:\\Windows\\Fonts\\NanumGothic.ttf").get_name()
rc('font', family=font_name)
wordcloud = WordCloud(
    font_path = 'C:\\Windows\\Fonts\\NanumGothic.ttf',    # 맥에선 한글폰트 설정 잘해야함.
    background_color='white',                             # 배경 색깔 정하기
    colormap = 'Accent_r',                                # 폰트 색깔 정하기
    width = 1000,
    height = 1000,
    max_words=max_words_num,
    max_font_size=300
) 

wordcloud_words = wordcloud.generate_from_frequencies(words)
"""
array = WordCloud.to_array()
print(type(array)) # numpy.ndarray
print(array.shape) # (800, 800, 3)
"""


#font_fname = "C:\\Windows\\Fonts\\NanumGothic.ttf"  # A font of your choice
#fontprop = fm.FontProperties(fname=font_fname, size=18)
#font_name=fm.FontProperties(fname=font_fname).get_name()  #print('-- font_name : ', font_name)
#plt.rc('font', family=font_name)

# 글씨 크기를 조정한 후의 워드 클라우드 작성하기
#wordcloud = WordCloud(max_font_size = 40).generate(wordcloud_words)
plt.figure(figsize = (12, 12))
plt.imshow(wordcloud_words, interpolation = "bilinear")
plt.axis("off")
plt.show()



