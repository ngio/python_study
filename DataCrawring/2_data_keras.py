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
