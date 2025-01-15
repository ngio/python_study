""" 
정렬 알고리즘 실행 시 비용 계산은 보통 실행 시간(시간 복잡도)이나 작업 횟수를 측정하여 이뤄집니다. 

이를 위해 Python에서 time 모듈이나 timeit 모듈을 사용할 수 있습니다. 

시간 복잡도에 따른 차이

1.퀵 정렬:
    평균 시간 복잡도 𝑂(𝑛log⁡𝑛)O(nlogn).
    큰 데이터셋에서도 효율적으로 작동.

2.버블 정렬:
    최악 및 평균 시간 복잡도 𝑂(𝑛2)O(n 2 ).
    작은 데이터셋에서는 괜찮지만, 데이터 크기가 클수록 비효율적.
    
"""
import time  # 실행 시간 측정을 위한 모듈

# 퀵 정렬 알고리즘
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 버블 정렬 알고리즘
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 테스트 데이터 생성
import random
array_size = 1000  # 데이터 크기
test_array = random.sample(range(1, 10000), array_size)


print(f" test_array : {test_array} \n\n\n")

# 퀵 정렬 실행 시간 측정
start_time = time.time()
quick_sort(test_array.copy())
end_time = time.time()
print(f"퀵 정렬 실행 시간: {end_time - start_time:.5f}초")

# 버블 정렬 실행 시간 측정
start_time = time.time()
bubble_sort(test_array.copy())
end_time = time.time()
print(f"버블 정렬 실행 시간: {end_time - start_time:.5f}초")


# 병합 정렬 알고리즘
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 병합 정렬 실행 시간 측정
start_time = time.time()
merge_sort(test_array.copy())
end_time = time.time()
print(f"병합 정렬 실행 시간: {end_time - start_time:.5f}초")
