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


