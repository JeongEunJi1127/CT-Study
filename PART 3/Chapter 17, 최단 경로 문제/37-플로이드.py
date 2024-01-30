import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = [[int(1e9) for _ in range(n)] for _ in range(n)]

# 시작 도시와 도착 도시가 같은 경우 0
for i in range(n):
    lst[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    # 가장 짧은 비용 정보로 저장
    lst[a-1][b-1] = min(lst[a-1][b-1],c)

# 플로이드 워셜 알고리즘 사용
for i in range(n):
    for j in range(n):
        for k in range(n):
            lst[j][k] = min(lst[j][k], lst[j][i]+lst[i][k])

for i in lst:
    for j in i:
        # 갈수 없는 도시인 경우 0으로 출력
        if j == int(1e9):
            print(0,end=" ")
        else:
            print(j,end=" ")
    print( )
