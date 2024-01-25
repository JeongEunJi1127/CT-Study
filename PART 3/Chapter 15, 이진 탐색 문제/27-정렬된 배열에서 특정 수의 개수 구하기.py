import sys
input = sys.stdin.readline
n,x = map(int,input().split())
lst = list(map(int,input().split()))

# 이진 탐색의 시간복잡도 : O(logN)
def binary_search(list,target,start,end):
    global cnt
    while start <= end:
        mid = (start+end) // 2
        # mid 값이 target보다 작으면 끝점을 mid-1로 두기
        if list[mid] > target:
            end = mid-1
        # mid 값이 target보다 크면 끝점을 mid+1로 두기
        elif list[mid] < target:
            start = mid+1
        # mid 값이 target과 같으면 중간값을 기준으로 왼쪽, 오른쪽 배열에서 이진탐색 시작
        else:
            # 답 += 1
            cnt+=1
            binary_search(list,target,mid+1,end)
            binary_search(list,target,start,mid-1)
            break
global cnt 
cnt = 0
binary_search(lst,x,0,n-1)
if cnt == 0:
    print(-1)
else:
    print(cnt)