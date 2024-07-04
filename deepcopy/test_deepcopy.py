"""_summary_
얕은 복사(shallow copy)
    list의 슬라이싱을 통한 새로운 값을 할당해봅니다.
    아래의 결과와 같이 슬라이싱을 통해서 값을 할당하면 새로운 id가 부여되며, 서로 영향을 받지 않습니다
"""

print("\n","*" * 30, "\n   얕은 복사(shallow copy) \n","*" * 30) 

a = [1, 2, 3]
b = a[:]
print(" a = ", a)
print(" b = ", b)

print(" id(a) : ", id(a)) #다른 주소
print(" id(b) : ", id(b))

print(" a == b : ", a == b)
print(" a is b : ", a is b)

b[0] = 5

print(a)
print(b)

""" 
    하지만, 이러한 슬라이싱 또한 얕은 복사에 해당합니다.
    리스트안에 리스트 mutable객체 안에 mutable객체인 경우 문제가 됩니다.
    id(a) 값과 id(b) 값은 다르게 되었지만, 그 내부의 객체 id(a[0])과 id(b[0])은 같은 주소를 바라보고 있습니다
"""
a = [[1,2],[3,4]]
b = a[:]
print(" id(a) : ", id(a)) #다른 주소
print(" id(b) : ", id(b))

print(" id(a[0]) : ",id(a[0])) #같은 주소
print(" id(b[0]) : ",id(b[0]))


"""깊은 복사(deep copy)
    깊은 복사는 내부에 객체들까지 모두 새롭게 copy 되는 것입니다.
    copy.deepcopy메소드가 해결해줍니다
"""
print("\n","*" * 30, "\n   deepcopy \n","*" * 30)  

import copy

a = [[1,2],[3,4]]
b = copy.deepcopy(a)
a[1].append(5)

print(" a : ", a)
print(" b : ", b)

print(" id(a) : ", id(a)) #다른 주소
print(" id(b) : ", id(b))

