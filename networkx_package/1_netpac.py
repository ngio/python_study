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

prePath = "./Project/networkx_package/"
file_name = prePath + "input/outputfile0.txt" 

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

# 한나눔 불러오기
from konlpy.tag import Hannanum
hannanum = Hannanum()

f = open(prePath + 'input/bigkinds_title01.txt','r', encoding='UTF-8')
lines = f.readlines()
print( len(lines) )
#print(lines)
f.close()

# 단어 2차원 리스트
dataset = []
for i in range(len(lines)):
    dataset.append(hannanum.nouns(re.sub('[^가-힣a-zA-Z\s]', '', lines[i])))
print(dataset[:10])

count = {}   #동시출현 빈도가 저장될 dict
for line in dataset:
    
    #하나의 문서에서 동일한 단어가 두번 나와도 두번의 동시출현으로 고려X
    #print(line)
    #words = list(set(line.split()))   
    words = list(set(line))   
    
    #한줄씩 읽어와서 단어별로 분리(unique한 값으로 받아오기)
    #split은 띄어쓰기를 단어로 구분하라는 함수     
    for i, a in enumerate(words):
        for b in words[i+1:]:
            if a>b: 
                count[b, a] = count.get((b, a),0) + 1  
            else :
                count[a, b] = count.get((a, b),0) + 1  
                
count.get(("a", "b"),0) #a, b라는 key가 없을 때는 디폴트를 0으로 해라 
#print(count)

#dictionary형 자료형을 판다스 데이터프레임으로 만들어줌 
#orient=index를 넣어야 행으로 쭉 나열이 됨 
df=pd.DataFrame.from_dict(count, orient='index')
print(df.head())


list1=[]
for i in range(len(df)):
    #index를 중심으로 계속 중첩해서 list에 넣는다 
    list1.append([df.index[i][0],df.index[i][1],df[0][i]])

#pandas 이용해서 df형태로 만들기 
df2 = pd.DataFrame(list1, columns=["term1","term2","freq"])    
#print(df2)

#pandas 이용해서 sorting 하기 (디폴트가 오름차순이라서 false 꼭 써줘야 내림차순으로 나옴)
df3 = df2.sort_values(by=['freq'],ascending=False)
#print(df3)
print(df3.head(100))

# Dataframe의 내용을 csv로 생성
## DataFrame.to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w'
#                    , encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None
#                    , doublequote=True, escapechar=None, decimal='.', errors='strict')
df3.to_csv(prePath + 'output/word_ex_note_1.csv', index = False, header=False, line_terminator=False, encoding='utf-8-sig')
df3.head(100).to_csv(prePath + 'output/word_ex_note_100.csv', header=False, line_terminator=False, encoding='utf-8-sig')
df3.to_csv(prePath + 'output/word_ex_note_1.txt', sep = '\t', index = False,header=False, line_terminator=False, encoding='utf-8-sig')
 

import numpy as np
import networkx as nx
import operator
#np.where는 조건문 만드는 것: (슬라이싱) 빈도가 5개 이상인 것만 잘라내면 1027개가 나온다. (참인 조건의 인덱스 추출)
len((np.where(df3['freq']>=5))[0])

G=nx.Graph()
for i in range(1027):
    #print(pair)    
    G.add_edge(df3['term1'][i], df3['term2'][i], weight=int(df3['freq'][i]))

# Compute centralities for nodes.
# The degree centrality values are normalized by dividing by the maximum possible degree in a simple graph n-1 where n is the number of nodes in G.
dgr = nx.degree_centrality(G)
btw = nx.betweenness_centrality(G)
cls = nx.closeness_centrality(G)

# itemgetter(0): key 또는 itemgetter(1): value로 sort key, reverse=True (descending order)
sorted_dgr = sorted(dgr.items(), key=operator.itemgetter(1), reverse=True)
sorted_btw = sorted(btw.items(), key=operator.itemgetter(1), reverse=True)
sorted_cls = sorted(cls.items(), key=operator.itemgetter(1), reverse=True)

print("** degree **")
for x in range(20):
    print(sorted_dgr[x])
print("** betweenness **")
for x in range(20):
    print(sorted_btw[x])
print("** closeness **")
for x in range(20):
    print(sorted_cls[x])


#단어끼리 서로 빈도를 세는 데이터셋을 만들었을 때 Gaphi로 시각화하는 것 전단계: graphml 확장자 형식으로 만들기
class MakeGraphml:
    def make_graphml(self, pair_file, graphml_file):
        out = open(graphml_file, 'w', encoding = 'utf-8')
        entity = []
        e_dict = {}
        count = []
        for i in range(len(pair_file)):
            e1 = pair_file.iloc[i,0]
            e2 = pair_file.iloc[i,1]
            #frq = ((word_dict[e1], word_dict[e2]),  pair.split('\t')[2])
            frq = ((e1, e2), pair_file.iloc[i,2])
            if frq not in count: count.append(frq)   # ((a, b), frq)
            if e1 not in entity: entity.append(e1)
            if e2 not in entity: entity.append(e2)
        print('# terms: %s'% len(entity))
        #create e_dict {entity: id} from entity
        for i, w in enumerate(entity):
            e_dict[w] = i + 1 # {word: id}
        out.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?><graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlnshttp://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\">" +
            "<key id=\"d1\" for=\"edge\" attr.name=\"weight\" attr.type=\"double\"/>" +
            "<key id=\"d0\" for=\"node\" attr.name=\"label\" attr.type=\"string\"/>" +
            "<graph id=\"Entity\" edgedefault=\"undirected\">" + "\n")
        # nodes
        for i in entity:
            out.write("<node id=\"" + str(e_dict[i]) +"\">" + "\n")
            out.write("<data key=\"d0\">" + i + "</data>" + "\n")
            out.write("</node>")
        # edges
        for y in range(len(count)):
            out.write("<edge source=\"" + str(e_dict[count[y][0][0]]) + "\" target=\"" + str(e_dict[count[y][0][1]]) + "\">" + "\n")
            out.write("<data key=\"d1\">" + str(count[y][1]) + "</data>" + "\n")
            #out.write("<edge source=\"" + str(count[y][0][0]) + "\" target=\"" + str(count[y][0][1]) +"\">"+"\n")
            #out.write("<data key=\"d1\">" + str(count[y][1]) +"</data>"+"\n")
            out.write("</edge>")
        out.write("</graph> </graphml>")
        print('now you can see %s' % graphml_file)
        #pairs.close()
        out.close()

gm = MakeGraphml()
graphml_file = prePath + 'output/netpac_001.graphml'

#iloc는 인덱스 index of location 열에서 : 써야 함 (열 전체 보여주려면)
gm.make_graphml(df3.iloc[0:1027,:], graphml_file)


#이게 끝인가? 
#Git test 2022-07-19
