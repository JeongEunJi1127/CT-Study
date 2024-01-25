# 고정점 : 수열의 값이 인덱스와 동일한 원소
# 수열에 정렬되어 있으므로 이진 탐색으로 중간값이 중간값의 인덱스 값보다 큰지 작은지 탐색

import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))

# 이진 탐색의 시간복잡도 : O(logN)
def binary_search(list,start,end):
    while start <= end:
        mid = (start+end) // 2
        # mid 값이 mid 인덱스보다 작으면 끝점을 mid+1로 두기
        if list[mid] > mid:
            end = mid-1
        # mid 값이 mid 인덱스보다 크면 끝점을 mid-1로 두기
        elif list[mid] < mid:
            start = mid+1 
        # mid 값이 mid 인덱스 값과 같으면 return mid
        else:
            return mid
        
    return -1
    
print(binary_search(lst,0,n-1))