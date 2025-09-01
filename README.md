# python_study 🐍
python, konply, numpy, matplotlib, networkx, pandas, Gradio

## opencv
pip install opencv-python은 OpenCV(Open Source Computer Vision Library)를 설치하기 위한 명령입니다. OpenCV는 이미지 처리와 컴퓨터 비전에 사용되는 강력한 라이브러리로, Python에서도 널리 사용됩니다.

<img src="./img/python-logo-generic.svg"  >  


 * 도서 - 친절한 파이썬 : https://wikidocs.net/book/17274  (2025-09-01)



[python] python, rust 의 관계 :  https://github.com/ngio/python_study/blob/main/python_rust_%EC%9D%98_%EA%B4%80%EA%B3%84.md

 

* 파일 실행에 필요한 모듈 리스트 추출 방법 : pipreqs 사용 (권장)

      pip install pipreqs

      pipreqs . --encoding=utf-8 --force


             .: 현재 디렉토리를 스캔하라는 의미입니다.
             
             --encoding=utf-8: 파일 인코딩을 지정합니다. (한글 주석 등이 있을 경우 필요)
             
             --force: 이미 requirements.txt 파일이 존재하더라도 덮어쓰도록 합니다. (주의해서 사용)


      pip install -r requirements.txt


2024-08-09 [TIOBE Index for August 2024 Python 1st](./TIOBE_Index_for_August_2024_Python_1st)


Kivy https://kivy.org/ 
https://wikidocs.net/book/8263

[Matplotlib Tutorial - 파이썬으로 데이터 시각화하기](https://wikidocs.net/book/5011)

[PDF to IMG ](Basic/pdf_to_png.py)

[PYTHON OCR 이미지 to 텍스트, image to Text](https://github.com/ngio/python_study/blob/main/pytesseract_image_to_text.py)


[Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)


Gradio  <em>Build & share delightful machine learning apps easily</em>

https://gradio.app/             
https://github.com/gradio-app/gradio   

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=25&pause=1000&color=40F718&width=435&lines=%EA%B8%8D%EC%A0%95%EC%A0%81%EC%9D%B8+%EC%82%AC%EA%B3%A0%2C+%EC%9D%8C%EC%8B%9D%EC%9D%98+%EC%A0%88%EC%A0%9C%2C+%EA%B7%9C%EC%B9%99%EC%A0%81%EC%9D%B8+%EC%9A%B4%EB%8F%99)](https://git.io/typing-svg)

[![GitHub Streak](https://streak-stats.demolab.com?user=ngio&theme=dark&locale=ko&mode=weekly)](https://git.io/streak-stats)

Turtle 🐢 : https://github.com/ngio/python_study/blob/main/Basic/Turtle_basic.md


![image](https://github.com/user-attachments/assets/49890301-fd8e-4865-984d-61fda72dd12c)


CoP : 학습공동체
[ 學習共同體 , Learning Community , Community of Practice ]

모든 학습자들이 각자 자신의 학습에 대하여 책임을 가지고 다른 구성원들의 학습을 서로 돕고 지원해주는 분위기가 형성된 특정 그룹을 의미한다. 유사한 흥미, 관심사, 공통의 가치, 믿음을 공유하는 사람들의 모임으로 학습의욕, 아이디어와 의견을 공유하려는 의지를 지닌 학습자 집단이다. 학습을 주목적으로 하는 개인들이 자발적으로 구성한 집단으로서, 구성원들이 협력적으로 상호작용하면서 학습에 새로운 가치를 부여하고 이를 통해 학습활동을 전개하는 학습경험을 공유하는 사람들의 집단이다.
[네이버 지식백과] 학습공동체 [學習共同體, Learning Community, Community of Practice] (HRD 용어사전, 2010. 9. 6., (사)한국기업교육학회)

*** CoP 운영기간 : 2022/11/18 ~ 2023/1/20, 7회 운영 
   학습주제 : Python 기본 문법 & 실습				
1. 운영목표 : 교재를 통해 Python 기본문법을 숙달하고, 간단한 프로그램 제작.				
2. 가입조건 : 프로그래밍 언어 유경험자, 관심이 많은 자				
3. 운영인원 : 6명 내외				
4. 학습활동 		
 - 1~2주차 : 설치, 기본문법(변수,자료형,연산)
 - 3~4주차 : 기본문법(조건문,반복문), 예외처리
 - 5~6주차 : 함수, 클래스
 - 7~9주차 : 교재내 예제 프로그램 개발


 * 참고교재: 모두의 파이썬(20일 만에 배우는 프로그래밍 기초)  https://thebook.io/007026/
            길벗 예제 - https://www.gilbut.co.kr/book/view?bookcode=BN002243#bookData

한곳에서 끝내는 파이썬 & 머신러닝 & 딥러닝 https://sdc-james.gitbook.io/onebook/        
        
2022-11-18
1주차 주제 : 엑셀이 없던 시절, 그 이후 
            개발 배우기가 정말 어려운 이유
            Python으로 무엇을 할 것인가? 
            내가 하고 싶은 것은?
            Python 설치 & 사용환경

2022-11-24
2주차 : 파이썬 설치 상태 확인 
        파이썬 모듈 설치하기 - https://docs.python.org/ko/3.7/installing/index.html
        기본문법 고고!   - https://wikidocs.net/11
           시작하기 : https://wikidocs.net/7014
           변수 : https://wikidocs.net/7021
           문자열 1 : https://wikidocs.net/7022
                  2 : https://wikidocs.net/7024
                  3 : https://wikidocs.net/78558
           리스트 1 : https://wikidocs.net/7023
                 2 : https://wikidocs.net/7025
            튜플 : https://wikidocs.net/7027
            딕셔너리 1 : https://wikidocs.net/22000
                    2 : https://wikidocs.net/78563
          
         워드클라우드 만들기


2022-11-30
3주차 : 제어문   
        전처리 (파일저장, 엑셀데이터 추출)
        빈도수 추출 한글 단어



2022-12-08
4주차 : 제어문 복습
        가상환경

        
        파이썬 모듈 설치하기 : https://docs.python.org/ko/3.10/installing/index.html

        1. 가상환경 내 python 버전 업그레이드
            가상환경 내 버전 변경하는 방법은 아래와 같습니다.
            (base) D:\_python_project\jupyter>conda search python
            
            명령어를 수행하면 설치 가능한 버전들이 나열이 됩니다.
            (base) D:\_python_project\jupyter>conda install python=3.8.0

            설치 후 버전 확인
            (base) D:\_python_project\jupyter>python -V

        2. 가상환경 만들기( python 버전 지정)
            가상환경 내 버전 변경하는 방법은 아래와 같습니다.
            (base) D:\_python_project\jupyter>conda search python
            
            명령어를 수행하면 설치 가능한 버전들이 나열이 됩니다.
            (base) D:\_python_project\jupyter>conda install python=3.8.0

            설치 후 버전 확인
            (base) D:\_python_project\jupyter>python -V


2022-12-15
5주차 : 함수, 지역변수, 전역변수, 입출력, 코딩시 표기법 '명명법'


2023-01-12
6주차 : 클래스, 모듈, 패키지
        - 환경변수, 디렉토리, 파일 
        - 인코딩
        클래스 : https://wikidocs.net/28
        모듈 : https://wikidocs.net/29
        패키지 : https://wikidocs.net/1418

2023-01-17
7주차 : CoP 내용정리 토론
        
        어려웠던 부분
        보람있었던 부분

        앞으로의 방향
         - 데이터 분석가는 ‘기획자’에 가깝고, 데이터 엔지니어와 사이언티스트는 ‘개발자’ 쪽에 가깝습니다. 
        빅데이터 : https://modulabs.co.kr/blog/category/bigdata/
        https://modulabs.co.kr/blog/data-analyst-2/




=======================================================================================================================



        CoP python 폴더 추가 [/python_study/CoP_study/](https://github.com/ngio/python_study/tree/main/CoP_study)
        
        Beginner Games : [/python_study/CoP_study/beginner_game/](https://github.com/ngio/python_study/tree/main/CoP_study/beginner_game)
        
        

[/python_study/CoP_study/](https://github.com/ngio/python_study/tree/main/CoP_study)

Beginner Game [/python_study/CoP_study/beginner_game/](https://github.com/ngio/python_study/tree/main/CoP_study/beginner_game)

[Python 3 Cheat Sheet](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)

[Python overapi](https://overapi.com/python)

[hyperpolyglot.org/scripting](https://hyperpolyglot.org/scripting)




# ‡‡ 왕초보를 위한 Python :       [Website](https://wikidocs.net/book/2)  연습문제 맛집
###    1.파이썬 시작하기           https://wikidocs.net/43
####    2.제어 구조                https://wikidocs.net/55
#####    2.1 while을 사용하는 반복문 https://wikidocs.net/56      https://youtu.be/j_NPpCNsfIM
#####    2.2 조건문(if-elif-else)   https://wikidocs.net/57
#####    2.3 for를 사용하는 반복문   https://wikidocs.net/58      https://youtu.be/TdFn4dnERHk
#####    2.4 match-case 문          https://wikidocs.net/173398
####    3. 함수                    https://wikidocs.net/86466
####    4. 데이터 타입             https://wikidocs.net/86707
####    5. 모듈                    https://wikidocs.net/132933
####    6. 파일                    https://wikidocs.net/132935
####    7. 객체지향                https://wikidocs.net/84
####    8.예외처리(try, except)    https://wikidocs.net/90
####    9. 테스팅과 성능            https://wikidocs.net/132931  




## /network/
### 1. nm.py : 빅카인즈 뉴스 데이터를 이용한 '깃대종' 통계 가시화, 국립공원이 언급된 깃대종 기사건수
### 1. nm_xls_extract.py : 엑셀 파일에서 원하는 시트의 셀만 가져오기
### 2. pandas.py : 빅카인즈 뉴스 데이터를 이용한 '깃대종' 연관규칙 분석, 어프라이어리(Apriori), 연관규칙(association rules)
        # 연관규칙(association rules)
        # 신뢰도(cofidence) : P(B|A) = P(A∩B) / P(A)
        # 형상도(lift) : P(B|A) / P(B)


## /DataCrawring/
### 1. datacrawring.py : json 형태 정보 웹페이지 beautifulsoup4로 가져와서 CSV로 저장하기
        #  
        #  
        #  
### 2. data_keras.py : 영화 평점,줄거리를 가지고 평점 예측 모델 만들기
