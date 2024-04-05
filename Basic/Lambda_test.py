"""  lambda function 
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

lambda 매개변수 : 표현식
함수를 딱 한 줄만으로 만들게 해주는 훌륭한 녀석
"""

x = lambda a : a + 10
print(' lambda a : a + 10 => ', x(5))

x = lambda a, b : a * b
print(' lambda a, b : a * b => ', x(5, 6))

x = lambda a, b, c : a + b + c
print(' lambda a, b, c : a + b + c => ', x(5, 6, 2))
 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
