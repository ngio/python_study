"""_summary_
    영화 평점,줄거리를 가지고 평점 예측 모델 만들기
    
    https://somjang.tistory.com/entry/Python%EC%98%81%ED%99%94-%ED%8F%89%EC%A0%90-%EC%A4%84%EA%B1%B0%EB%A6%AC%EB%A5%BC-%EA%B0%80%EC%A7%80%EA%B3%A0-%ED%8F%89%EC%A0%90-%EC%98%88%EC%B8%A1-%EB%AA%A8%EB%8D%B8-%EB%A7%8C%EB%93%A4%EC%96%B4%EB%B3%B4%EA%B8%B0feat-Keras?category=349595
    
    네이버 시리즈온 영화 전체
    https://serieson.naver.com/v2/movie/products
    https://apis.naver.com/seriesOnWeb/serieson-web/v2/movie/products?ero=false&orderType=RECENT_REGISTRATION&offset=0&limit=31&_t=1649039368714
"""
import os
import sys
os.environ['JAVA_OPTS'] = 'Xmx4096M'
    
import re
import pandas as pd
import numpy as np
import json
 
import seaborn as sns
sns.set(style='darkgrid',font='KoPubDotum', font_scale=1.5 )
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 폰트 관련 용도

font_fname = "C:/Windows/Fonts/NanumGothic.ttf"  # A font of your choice
fontprop = fm.FontProperties(fname=font_fname, size=18)
font_name=fm.FontProperties(fname=font_fname).get_name()  #print('-- font_name : ', font_name)
plt.rc('font', family=font_name)

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

prePath = "./Project/DataCrawring/"
file_name = prePath + "input/movie_data_1649226040.csv" 

import warnings
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always") 
print(file_name)  
#df  = pd.read_excel(file_name, sheet_name='sheet', index_col='일자', parse_dates=True, engine="openpyxl")
movie_df = pd.read_csv(file_name)
movie_df.info()


### # clean synopsis column add , update save
### print(movie_df['synopsis'].str.replace(pat=r'[^\w]',repl=r' ',regex=True))  # 특수문자 제거
### movie_df.insert(2, "clean_synopsis", movie_df['synopsis'].str.replace(pat=r'[^\w]',repl=r' ',regex=True))
### print(movie_df[31:40])
### movie_df.to_csv(file_name, index=False, mode='w', header=True, line_terminator=False, encoding='utf-8-sig')

x_data = movie_df['clean_synopsis']  # 특수문자제거 줄거리
y_data = movie_df['starScore']       # 영화 평점

# 줄거리를 토큰화하고 각각의 토큰을 숫자로 변경하였습니다.
from keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_data)
sequences = tokenizer.texts_to_sequences(x_data)
word_index = tokenizer.word_index
print(word_index)


vocab_size = len(tokenizer.word_index) + 1 # 패딩을 고려하여 +1
print('단어 집합 :',vocab_size)

print('줄거리의 최대 길이 : {}'.format(max(len(l) for l in x_data)) )
print('줄거리의 평균 길이 : {}'.format(sum(map(len, x_data)) / len(x_data)))
plt.hist([len(s) for s in x_data], bins=50)
plt.xlabel('length of Data')
plt.ylabel('number of Data')
#plt.show()


from keras.datasets import reuters
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
from keras.preprocessing import sequence
from keras.preprocessing.sequence import pad_sequences  # 패딩을 위해 pad_sequences()를 제공
from keras.utils import np_utils
import seaborn as sns


max_len = 250
X_train = pad_sequences(sequences, maxlen=max_len, padding='post')
y_train = np_utils.to_categorical(y_data)
 
print('패딩 결과 :')
print(X_train)

embedding_dim = 4


model3 = Sequential()
model3.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
model3.add(LSTM(120))
model3.add(Dense(11, activation='softmax'))
model3.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
#model3.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

history = model3.fit(X_train, y_train, epochs=10, batch_size=10)

print("\n 테스트 정확도 : %.4f" % (model3.evaluate(X_train, y_train)[1]))

