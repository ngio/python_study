 
"""
3주차 교육
     수요일(11월 30일) GS.A 오후 2시 30분~ 4시 30분까지 진행
3주차 : 제어문
     전처리
     빈도수 추출 한글 단어
     단어 추가
     추출 단어 파일 저장
"""     
     
     
title = [ "3주차 교육"
         ,"3주차 : 제어문","     전처리","     빈도수 추출 한글 단어"
         ,"     단어 추가","     추출 단어 파일 저장"]

print(type(title), "의 길이는 ", len(title) ,"\n\n")


i = 0 # 변수 초기화
while i < len(title):
    print(title[i])
    i = i + 1  # 변수 1씩 증가해서 위 while 문 조건절을 나가야 한다.

title_str = ''.join(title)    # 리스트의 문자열을 모두 하나의 문장으로 합친다.
print( "\n\n", type(title_str), "의 길이는 ", len(title_str) ,"\n\n")


pprint(title_str)


a = [(1,2), (3,4), (5,6)]
type(a)

2 * 2 =  
2* 3 = 



""" IF  https://wikidocs.net/20
    조건문에서 "조건문"이란 참과 거짓을 판단하는 문장을 말한다. 
"""
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
    
""" IF  다중 조건 판단을 가능하게 하는 elif """
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
     print("택시를 타고가라 1")
elif card: 
     print("택시를 타고가라 2")
else:
     print("걸어가라")
     
     
""" IF 조건부 표현식 
    변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값
"""
score = 50

if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

message1 = "success" if score >= 60 else "failure " 
print(message1)





""" while   https://wikidocs.net/21
    반복해서 문장을 수행해야 할 경우
    while문은 조건문이 참인 동안에 while문에 속한 문장들이 반복해서 수행
"""
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    #if(treeHit == 3):
    #    break;          ### while문 강제로 빠져나가기
    print("ing~")

    if treeHit == 10:
        print("나무 넘어갑니다.")
        
        
print("end")



coffee = 3
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break


""" while문의 맨 처음으로 돌아가기 """
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
    
    
    

""" for 문  https://wikidocs.net/22
    리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입되어 "수행할 문장1", "수행할 문장2" 등이 수행된다.

"""
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
    
    
    
    
for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(i*j, end=" ") 
    print('') 
    ""
for i in range(2,10):        # 1번 for문
    gugu = ""
    for j in range(1, 10):   # 2번 for문
        gugu += str(i*j)
    print( gugu,' ')     




marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print( number, "번 학생은 합격입니다.")
    else: 
        print("%d %s 번 학생은 불합격입니다." % (number , number)  )
number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)     
    
    

""" 한글 형태소
    # pip install konlpy
    # https://konlpy.org/ko/latest/api/konlpy.tag/#konlpy.tag._kkma.Kkma
"""
from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()
pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'), depth=1)  # pprint :  아름답게 들여쓰기
pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))



""" 형태소 분석 및 품사 태깅
    # https://konlpy.org/ko/latest/morph/
"""
from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()
verse = "아이폰 기다리다 지치어 애플공홈에서 언락폰질러버렸다 128기가실벜"
pprint(kkma.sentences(verse), depth=1) # 문장 단위로 끊어본다
pprint(kkma.nouns(verse)) # 명사
pprint(kkma.pos(verse))    # 구성요소 태깅
pprint(kkma.morphs(verse)) # 형태소 단위



"""
    리스트 컴프리헨션 사용하기  https://wikidocs.net/22#_1
    : 리스트 안에 for문을 포함하는 리스트 컨프리헨션(List comprehension)
"""
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

print(" 리스트  for문으로 변환")
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)


    
