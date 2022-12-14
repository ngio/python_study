"""
   week_03_데이터전처리_엑셀 데이터 추출
   
   Pandas의 read_excel을 이용하면 엑셀 파일을 python의 dataframe으로 불러올 수 있다.
"""
import os
os.getcwd()  # 현재 디렉토리 경로 확인 , 작업하는 경로(위치)가 어디인지 확인

# pip install xlrd
# pip install openpyxl
# pip install pandas

# Pandas
import pandas as pd

pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx')



# xlsx to CSV
xlsx = pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = 2, names = ['col1', 'col2'])
xlsx.to_csv("D:\\python\\jupyter_data\\notebook\\word_0_1.csv", index = False)

# CSV 읽어들이기 
csv_test = pd.read_csv('D:\\python\\jupyter_data\\notebook\\word_0_1.csv')
csv_test


#  text 파일로 저장하기
xls_text = pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = '1.전체', usecols = ['내용'] )
type(xls_text)

# xlsx to txt
# xlsx = pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = 2, names = ['col1', 'col2'])
xls_text.to_csv("D:\\python\\jupyter_data\\notebook\\word_0_1.txt")

# - 저장할때 인덱스 없이 저장
#xls_text.to_csv("D:\\python\\jupyter_data\\notebook\\word_0_1.txt", index = False) 


# 구분자 변경 Tab으로 구분
#xls_text.to_csv("D:\\python\\jupyter_data\\notebook\\word_0_1.txt", sep = '\t')

#  파일 읽어 들이기
f = open("D:\\python\\jupyter_data\\notebook\\word_0_1.txt" , "rt", encoding="utf-8-sig")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()





# 이름으로 불러오기
pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = '1.전체')


# 번호로 불러오기 (시작이 0)
pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = 2)  # 2.사업범위


# names : 열 이름 변경
pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = 2, names = ['col1', 'col2'])

# usecols : 불러올 열 지정
# 이름으로 불러오기
pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = '1.전체', usecols = ['내용'] )

# usecols : 불러올 열 지정
# 번호로 지정
pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx',sheet_name = '1.전체' , usecols = [1])

# usecols : 불러올 열 지정
# 열 이름 변경해서 이변경된 이름으로 불러오기
pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = '1.전체', names = ['col1', 'col2'], usecols = ['col2'] )

# na_values : 결측값 인식하기  - 결측값(NA / NaN)으로 인식 할 문자열 지정
# - '', '# N / A', '# N / AN / A', '#NA', '-1. # IND', '-1. # QNAN', '-NaN', '-nan', '1. # IND', '1. # QNAN', '<NA>', 'N / A', 'NA', 'NULL', 'NaN', 'n / a ','nan ','null '는 기본적으로 결측값으로 인식된다.
pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = 0 , na_values = '-')

## 불러올 행 제한
#  nrows : 불러올 행 개수 제한 / 처음 ~ n번째 행만 불러오기 
#  skiprows : 처음 ~ n번째 행 제외 / n+1번째 ~ 마지막까지
#  skipfooter : 뒤에서 n개 제외

pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = '1.전체', names = ['col1', 'col2'], skiprows = 1)   # 앞에서 n개 행 생략


pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = '1.전체', nrows = 5)   # 처음 ~ n번째

pd.read_excel('D:\\python\\jupyter_data\\notebook\\word_0.xlsx', sheet_name = '1.전체', skipfooter = 9)   # 뒤에서 n개 행 생략

