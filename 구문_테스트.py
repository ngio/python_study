""" 
# What will be the output?
    A.Infinite loop
    B.120
    C.47
    D.48
"""
import secrets


def rec(a,b):
    if a == 0:
        return b
    else:
        return rec(a - 1, a + b)

print(rec(8, 12))

# 48 


s1 = [92,57,[82,75]]
s2 = s1[:]
s2[2][1] = 23
print(s1)

# 클래스 
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))


"""
    # what will be the output?
    A.@corporate
    B.qna
    C.corporate
    D.@qna
"""
s = ['@corporate','qna']
print(s[:-1][-1])



import FourCal  #FourCal.py
"""
class FourCal:
    #def __init__(self, first, second):
    #    self.first = first
    #    self.second = second    
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
"""
    
a = FourCal.FourCal(4,2)

a.add()

