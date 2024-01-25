import sys
input = sys.stdin.readline
n,c = map(int,input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

# 공유기 사이 최소 거리 1로 설정
start = 1
# 공유기 사이 최대 거리 end =  houses[-1] - houses[0]
end = houses[-1] - houses[0]

def binary_search(list,start,end):
    ans = 0
    while start <= end:
        # 현재 공유기 사이 거리
        mid = (start+end) // 2
        print(start,end,mid)
        # 설치할 수 있는 공유기의 수
        cnt = 1
        prev = houses[0]
    
        for i in range(len(houses)):
            if houses[i] >= mid + prev:
                cnt += 1
                prev = houses[i]
        # 현재 거리 mid 사이에서 설치할 수 있는 공유기의 수가 주어진 수 c보다 크거나 같으면 공유기 사이 거리 늘림
        if cnt >= c:
            start = mid+1
            ans = mid
        # 현재 거리 mid 사이에서 설치할 수 있는 공유기의 수가 주어진 수 c보다 작으면 공유기 사이 거리 줄임
        else:
            end = mid-1
    return ans
    
print(binary_search(houses,start,end))
                
