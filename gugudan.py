# [파이썬] 간단한 구구단 프로그램 만들기  
 
 
# 구구단 특정 단수 입력 받아서 출력
def guguNormal(n):
    for m in range(2, 10):
        print(f'{n} x {m} = {n * m}')  # f스트링 이용
 
 
# 구구단 세로 출력
def guguVertical():
    for n in range(1, 10):  # 단 수가 밖에 존재.
        for m in range(2, 10):
            print(f'{n} x {m} = {n * m}')  # f스트링 이용
 
 
# 구구단 가로 출력
def guguHorizontal():
    for m in range(2, 10):
        for n in range(1, 10):  # 단 수가 안에 들어왔다.
            print(f'{n} x {m} = {n * m}', end='\t')
        print()

 
# 메인 while 루프 입니다.

print("구구단 프로그램 시작...")

while True:
    print("=" * 30)         # "="를 30개 출력
    print("1. 특정 단수 세로로 출력.")
    print("2. 1~9단 까지 세로로 출력.")
    print("3. 1~9단 까지 가로로 출력.")
    print("4. 프로그램 종료")
    print("=" * 30)
    print("입력 : ", end="")  # end=""는 print 하고 다음줄로 넘어가지 않겠다는 뜻
    num = int(input())       # 첫번째 입력 받고 int 타입으로 받습니다
    if num == 1:  # 특정 단수 입력
        print("단수를 입력하세요 : ", end='')
        n = int(input())  # 몇단을 원하는지 입력받음.
        guguNormal(n)
    elif num == 2:  # 세로
        guguVertical()
    elif num == 3:  # 가로
        guguHorizontal()
    elif num == 3:
        break  # 프로그램 종료
    else:
        print("1~4 사이의 숫자를 입력해주세요")  # 1~3 번호가 아닐 때 예외처리
      
      
      
      
