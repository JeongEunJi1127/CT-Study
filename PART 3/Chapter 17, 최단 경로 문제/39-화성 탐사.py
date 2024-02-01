import sys
import heapq
input = sys.stdin.readline

# 남동북서
dx = [0,1,0,-1]
dy = [1,0,-1,0]

t = int(input())

for _ in range(t):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    # 최소 비용 저장할 2차원 리스트
    distance = [[int(1e9)] * n for _ in range(n)]

    x,y = 0,0
    # x에서 y로 가는 비용, x, y
    q = [(lst[x][y], x,y)]
    distance[x][y] = lst[x][y]

    while q:
        dist,x,y = heapq.heappop(q)
        # x,y에 대해 저장되어 있는 최단 경로 값이 새로 확인해 볼 최단 경로 값보다 작으면 굳이 실행하지 않아도 됨
        if distance[x][y] < dist:
            continue
        # 4방위 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 배열 인덱스 값 넘어가는지 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + lst[nx][ny]
            if cost < distance[nx][ny]:
                 distance[nx][ny] = cost
                 heapq.heappush(q,(cost,nx,ny))
    
    print(distance[n-1][n-1])