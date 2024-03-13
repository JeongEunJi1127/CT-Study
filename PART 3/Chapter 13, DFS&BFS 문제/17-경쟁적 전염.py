from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
matrix = []
data = [] 

for i in range(n):
    matrix.append(list(map(int,input().split())))
    for j in range(n):
        if matrix[i][j] != 0:
            # 바이러스 종류, 시간, 위치x, 위치y
            data.append((matrix[i][j],0,i,j))
s,x,y = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,-1,1]

data.sort()
queue = deque(data)

while queue:
    now_virus,ns,nx,ny = queue.popleft()
    if ns == s:
        break
    for i in range(4):
        nowx,nowy = nx+dx[i], ny+dy[i]
        if nowx<0 or nowx>=n or nowy<0 or nowy>=n:
            continue
        elif matrix[nowx][nowy] == 0:
            matrix[nowx][nowy] = now_virus
            queue.append((now_virus,ns+1,nowx,nowy))

print(matrix[x-1][y-1])