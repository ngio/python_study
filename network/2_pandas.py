"""
https://blog.daum.net/geoscience/1407  : 빅카인즈 뉴스 데이터를 이용한 '깃대종' 연관규칙 분석

"""
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

#트래잭션 인코더
# pandas : 파이썬에서 사용하는 데이터분석 라이브러리로, 행과 열로 이루어진 데이터 객체를 만들어 다룰 수 있게 되며 보다 안정적으로 대용량의 데이터들을 처리하는데 매우 편리한 도구
# mlxtend :  일상적인 데이터 사이언스 작업에 유용한 도구들로 구성된 파이썬 라이브러리
print(" #트래잭션 인코더 ")
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
# 주어진 코드에서 fit 함수를 통해 dataset은 고유한 라벨을 갖게 되고 , transform함수를 통해서 파이썬 리스트를 one-hot 인코딩 된 numPy 배열로 변환합니다.
te_ary = te.fit(dataset).transform(dataset)  
df = pd.DataFrame(te_ary, columns=te.columns_)
df_list = df[['깃대종', '국립공원', '속리산', '발행', '가야산', '변산반', '오대산']].head()
print(df_list)

#어프라이어리(Apriori) 
from mlxtend.frequent_patterns import apriori, association_rules  
# 항목 개수가 2개이고 지지도(support)가 0.01 이상인 항목집합만 추려낸 결과입니다.
#지지도(support) : P(A∩B)
print(" #지지도(support) : P(A∩B) ")
frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)
print(frequent_itemsets)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

#  항목 개수가 2개이고 지지도(support)가 0.01 이상인 항목집합만 추려낸 결과입니다.
frequent_list = frequent_itemsets[(frequent_itemsets['length'] == 2) & (frequent_itemsets['support'] >= 0.01)].sort_values(by='support', ascending=False).head(10)
print(frequent_list)
