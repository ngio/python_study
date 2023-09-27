# 정렬/탐색 알고리즘 : https://modulabs.co.kr/blog/algorithm-python/
# Search 탐색 

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def hash_search(list, target):
    hash_table = {}
    for i in range(0, len(list)):
        hash_table[list[i]] = i
    if target in hash_table:
        return hash_table[target]
    return None

def brute_force_search(list, target):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == target:
                return [i, j]
    return None

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True 
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)







print(linear_search([1,2,3,4,5], 5)) 

print(binary_search([1,2,3,4,5], 5))

print(hash_search([1,2,3,4,5], 5))

print(brute_force_search([1,2,3,4,5], 5))

print(recursive_binary_search([1,2,3,4,5], 5))