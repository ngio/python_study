## FIZZBUZZ
# 피즈 버즈(fizz buzz 또는 FizzBuzz)는 아이들에게 나눗셈을 가르치는 단어 게임입니다. 플레이어는 자기 차례가 되면 숫자를 증가시키되, 3으로 나누어 떨어지는 숫자는 ‘피즈(Fizz)’로, 5로 나누어 떨어지는 숫자는 ‘버즈(Buzz)’로 바꿉니다.
# 1, 2, 피즈, 4, 버즈, 피즈, 7, 8, 피즈, 버즈, 11, 피즈, 13, 14, 피즈 버즈, 16, 17, 피즈, 19, 버즈, 피즈, 22, 23, 피즈, 버즈, 26, 피즈, 28, 29, 피즈 버즈, 31, 32, 피즈, 34, 버즈, 피즈, ...

 
"""The module provides two functions, fizzbuzz and fizzbuzz_extended
"""
from __future__ import print_function
import os
os


def fizzbuzz(n):
    """return a fizzbuzz-formatted representation of n"""
    if n == 0:
        return str(0)
    out = ''
    if not n % 3:
        out += 'Fizz'
    if not n % 5:
        out += 'Buzz'
    if not out:
        out = str(n)
    return out


def fizzbuzz_extended(n, additional={}):
    """return a fizzbuzz-formatted representation of n, with extensions

    If passed, the `additional` arg should be a dictionary keyed by integer
    with the values being the desired string substitution for that integer
    """
    if n == 0:
        return str(0)
    base = {3: 'Fizz', 5: 'Buzz'}
    base.update(additional)
    out = ''
    for x in sorted(base.iterkeys()):
        if not n % x:
            out += base[x]
    if not out:
        out = str(n)
    return out


if __name__ == '__main__':
    print("FizzBuzz Produces:")
    for i in xrange(100):
        print(fizzbuzz(i), end=" ")
    print()
    others = {7: 'Sizz', 11: 'Elzz'}
    for i in xrange(100):
        print(fizzbuzz_extended(i, others), end=" ")
    print()

