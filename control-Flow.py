""" Python Control-Flow
    if
    if - else
    for
    while
    break
    continue
"""


print("----- if, if - else")
a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b equal")
    
    
print("----- for")
fruits = [ "apple", "banana", "cherry"]    
for x in fruits:
    print(x)
    

print("----- while, break")    
i = 1
while i < 6:
    print(i)    
    if( i == 3 ):
        break
    i += 1

    
print("----- continue")
i = 0
while i < 6: 
    i += 1   
    if( i == 3 ):
        continue
    print(i)

    
    
