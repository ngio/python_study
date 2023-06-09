##  인스타그램 이미지 크롤링
#    
##
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

prePath = "./Project/instagram_cr/"
file_name = prePath + "outputfile0.txt" 

# 라이브러리 추가
from bs4 import BeautifulSoup  #불러온 데이터를 구분지어 원라는 데이터 출력
from selenium import webdriver #Chromedriver를 사용하여, 자동화 시스템 구동
## chrome 버전 안맞으면 아래와 같은 에러 발생함. chromedriver 버전 확인 필수
#  selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 94
# Current browser version is 105.0.5195.102 with binary path C:\Program Files\Google\Chrome\Application\chrome.exe
# 
# GoUrl : https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52/
##


from urllib.request import urlopen
from urllib.parse  import quote_plus # ASCII 형태로 자동 변형
import requests
import shutil
 


testurl_01 = "https://www.instagram.com/explore/tags/"
testurl_02 = input("Please input the word to search for : ")
testurl_03 = testurl_01 + quote_plus(testurl_02)


print(testurl_03)

## 아래 오류때문에 추가함. options
#  USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. 
## options start
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#browser = webdriver.Chrome(options=options)
## options end 

#driver_01 = webdriver.Chrome()
driver_01 = webdriver.Chrome(options=options)
driver_01.get(testurl_03)

html_01 = driver_01.page_source
#print(html_01)

Source_01 = BeautifulSoup(html_01,"html.parser")
#Source_01 = BeautifulSoup(html_01,"lxml")
#Source_01 = BeautifulSoup(html_01)

time.sleep(5)

#print(Source_01)
print(Source_01.prettify())
 
o = open(prePath +'result_list.txt', 'w', encoding='utf-8')
o.write("")
o.write(Source_01.prettify())
o.close()    




var_list = [1, 3, 5, 7, 9]
for ii in var_list:
    print("----------------------------------------")


Demo_insta = Source_01.select('._a3wf._-kb.segoe') 
print(Demo_insta)

for each_div in Source_01.findAll('div',{'class':'list'}):
    print(each_div)


"""
x_1 = 1

for i in Demo_insta:
    print("https://www.instagram.com/" + i.a['href'])
    #img_01 = i.select_one('_aagt').img['src']
    #print(img_01)
"""

driver_01.close()
