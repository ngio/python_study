#Python - Searching Algorithms
#
# https://www.tutorialspoint.com/python_data_structure/python_searching_algorithms.htm
#
#Linear Search
#선형 검색
#이 검색 유형에서는 모든 항목에 대해 하나씩 순차적 검색이 수행됩니다. 모든 항목을 검사하고 일치하는 항목이 발견되면 해당 항목이 반환되고, 그렇지 않으면 데이터 구조가 끝날 때까지 검색이 계속됩니다.

def linear_search(values, search_for):
   search_at = 0
   search_res = False
# Match the value with each data element	
   while search_at < len(values) and search_res is False:
      if values[search_at] == search_for:
         search_res = True
      else:
         search_at = search_at + 1
   return search_res
l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l, 12))
print(linear_search(l, 91))

#Interpolation Search
#보간 검색
#이 검색 알고리즘은 필요한 값의 프로빙 위치에서 작동합니다. 이 알고리즘이 제대로 작동하려면 데이터 컬렉션이 정렬된 형태로 균등하게 분산되어야 합니다. 처음에 프로브 위치는 컬렉션의 가장 중간 항목 위치입니다. 일치하는 경우 항목의 인덱스가 반환됩니다. .가운데 항목이 항목보다 큰 경우 프로브 위치는 중간 항목 오른쪽에 있는 하위 배열에서 다시 계산됩니다. 그렇지 않으면 중간 항목 왼쪽에 있는 하위 배열에서 항목이 검색됩니다. 이 프로세스는 하위 배열의 크기가 0으로 줄어들 때까지 하위 배열에서도 계속됩니다.
def intpolsearch(values, x):
    idx0 = 0
    idxn = len(values) - 1

    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:
        # Find the mid point
        mid = idx0 + int(((float(idxn - idx0) / (values[idxn] - values[idx0])) * (x - values[idx0])))

        # Compare the value at mid point with search value
        if values[mid] == x:
            return "Found " + str(x) + " at index " + str(mid)
        if values[mid] < x:
            idx0 = mid + 1
        else:
            idxn = mid - 1

    return "Searched element not in the list"

l = [2, 6, 11, 19, 27, 31, 45, 121]
print(intpolsearch(l, 2))