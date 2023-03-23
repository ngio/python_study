""" 
# What will be the output?
    A.Infinite loop
    B.120
    C.47
    D.48
"""
def rec(a,b):
    if a == 0:
        return b
    else:
        return rec(a - 1, a + b)

print(rec(8, 12))

# 48 
