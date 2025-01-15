""" 
1. 버블 정렬 (Bubble Sort)
    특징: 인접한 두 요소를 비교하여 순서를 바꾸는 방식. 배열이 정렬될 때까지 반복.
    시간 복잡도:
    최선: 𝑂(𝑛) O(n) (이미 정렬된 경우)
    평균 및 최악: 𝑂(𝑛2) O(n 2 )
    장점: 구현이 매우 간단.
단점: 비효율적이고 큰 배열에서는 성능이 좋지 않음.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 마지막 i개의 요소는 이미 정렬되어 있으므로 비교하지 않음
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 인접한 요소를 스왑
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 테스트용 배열
arr = [64, 34, 25, 12, 22, 11, 90]

print("정렬 전 배열:", arr)
sorted_arr = bubble_sort(arr)
print("정렬 후 배열:", sorted_arr)

print(".")

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 교환이 한 번도 이루어지지 않으면 정렬 완료
        if not swapped:
            break
    return arr

# 테스트
arr = [64, 34, 25, 12, 22, 11, 90]

print("정렬 전 배열:", arr)
print("정렬 후 배열:", optimized_bubble_sort(arr))
