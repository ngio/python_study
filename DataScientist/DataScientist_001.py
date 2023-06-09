### 데이터 과학자를 위한 6가지 Python 팁
### Top 6 Python Tips for Data Scientists
### https://towardsdatascience.com/top-6-python-tips-for-data-scientists-4f4a25e44d15

codeString = '''a,b = 4,5; print(f"a = {a} and b = {b}"); print(f"a+b = {a+b}")'''
exec(codeString)

print("\n\n\n")


import os
import sys

#작업하는 경로(위치)가 어디인지 확인
print(os.getcwd())


exec(open("./Project/Datascientist/myFullFileName.py").read())

print("\n\n\n")

### 각각 현재 작업 디렉토리 또는 사용자 지정 디렉토리의 모든 파일을 나열합니다.
print( os.listdir() )



"""_summary_
"""
print("\n\n\n")

### 4. Code timer as a decorator 
import time
import requests

def timerWrapper(func):
    """Code the timer"""

    def timer(*args, **kwargs):
        """Start timer"""
        start = time.perf_counter()
        
        output = func(*args, **kwargs)
        
        timeElapsed = time.perf_counter() - start
        print(f"Current function: {func.__name__}\n Run Time: {timeElapsed}")
        return output

    return timer

## Func to make a request to an user-defined url
@timerWrapper
def getArtile(url):
    return requests.get(url, allow_redirects=True)

## Monitor the runTime 
if __name__ == "__main__":
    getArtile('https://towardsdatascience.com/6-sql-tricks-every-data-scientist-should-know-f84be499aea5')
    

print("\n\n\n")
    
## 이제 다른 함수의 시간을 측정 @timeWrapper하려면 함수 앞에 the를 놓는 것뿐입니다.
@timerWrapper
def getMultiplication(num):
    for val in range(num):
        print(10**(10**val))

getMultiplication(3)            
