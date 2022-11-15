"""
 Calculator 계산기
 
  : 사칙연산 계산기
  
"""

def 더하기(a, b):
    return a + b

def 빼기(a, b):
    return a - b

def 곱하기(a, b):
    return a * b

def 나누기(a, b):
    return a // b

while True:
    print('계산기 종료 : 0')
    number1 = int(input('첫번째 숫자를 적으세오 > '))
    if (number1 == 0 ):
        print('good - bye!')
        break
    부호 = str(input(' +, -, *, / 고르세요 > '))
    number2 = int(input('두번째 숫자를 적으세요 > '))

    if (부호 == '+'):
        r = 더하기(number1, number2)

    elif (부호 == '-'):
        r = 빼기(number1, number2)

    elif (부호 == '*'):
        r = 곱하기(number1, number2)

    elif (부호 == '/'):
        r = 나누기(number1, number2)

    else:
        print('"{}" 잘못된 입력'.format(부호))


    print(' 결과 : {} {} {} = {}'.format(number1, 부호, number2, r))
