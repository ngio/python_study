""" 
퀵 정렬(Quick Sort)은 분할 정복(Divide and Conquer) 전략을 사용하여 리스트를 정렬하는 효율적인 알고리즘입니다. 

퀵 정렬은 큰 데이터셋에서 매우 효율적이며, 실제로 자주 사용되는 정렬 알고리즘 중 하나입니다.

퀵 정렬 작동 원리
1.피벗 선택: 리스트에서 하나의 요소를 피벗(pivot)으로 선택합니다.
2.분할: 피벗을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽으로 나눕니다.
3.재귀 호출: 분할된 리스트에 대해 재귀적으로 퀵 정렬을 수행합니다.
4.병합: 모든 분할이 완료되면 정렬된 리스트가 완성됩니다.

"""


def quick_sort(arr):
    # 종료 조건: 리스트의 길이가 1 이하이면 정렬된 상태
    if len(arr) <= 1:
        return arr
    
    # 피벗 선택 (중간 요소 선택)
    pivot = arr[len(arr) // 2]
    
    # 피벗보다 작은 요소
    left = [x for x in arr if x < pivot]
    # 피벗과 같은 요소
    middle = [x for x in arr if x == pivot]
    # 피벗보다 큰 요소
    right = [x for x in arr if x > pivot]
    
    # 분할한 세 부분을 재귀적으로 정렬
    return quick_sort(left) + middle + quick_sort(right)

# 테스트
arr = [33, 10, 68, 19, 72, 50, 24]

print("정렬 전 배열:", arr)

sorted_arr = quick_sort(arr)

print("정렬된 리스트:", sorted_arr)


