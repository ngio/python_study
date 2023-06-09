"""_summary_
    json 형태 정보 웹페이지 beautifulsoup4로 가져와서 CSV로 저장하기
    
    네이버 시리즈온 영화 전체
    https://serieson.naver.com/v2/movie/products
    https://apis.naver.com/seriesOnWeb/serieson-web/v2/movie/products?ero=false&orderType=RECENT_REGISTRATION&offset=0&limit=31&_t=1649039368714
"""
import os
import sys
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

"""        
def getPageLinks(pageRange):
    links = []
    
    for pageNo in range(pageRange):
        url = "https://apis.naver.com/seriesOnWeb/serieson-web/v2/movie/products?ero=false&orderType=RECENT_REGISTRATION&offset="+ str(pageNo) +"&limit=31&_t=1649039368714"
        url = "https://serieson.naver.com/v2/movie/products"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        movielinks = soup.select("div.content_list_con ul li a[href]")
        
        for movielink in movielinks:
            link = str(movielink.get('href'))
            links.append("https://serieson.naver.com"+link)
    return links

def getPageLinksWantRange(startPageNo, lastPageNo):
    links = []
    return_links = []
    
    for pageNo in range(startPageNo-1, lastPageNo):
        url = "https://apis.naver.com/seriesOnWeb/serieson-web/v2/movie/products?ero=false&orderType=RECENT_REGISTRATION&offset="+ str(pageNo+1) +"&limit=31&_t=1649039368714"
        url = "https://serieson.naver.com/v2/movie/products"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        movielinks = soup.select("div.content_list_con ul li a[href]")
        
        for movielink in movielinks:
            link = str(movielink.get('href'))
            links.append("https://serieson.naver.com"+link)
    return links
"""   
