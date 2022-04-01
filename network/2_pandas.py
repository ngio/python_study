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
