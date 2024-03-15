from collections import deque
# bfs 문제

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
# 상어 크기, 상어가 먹은 물고기 수, 거리
size, cnt, second = 2,0,0
# 상어 위치
x,y = 0,0
  
def go(mat,x,y):
    board = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    queue = deque([(x,y)])
    visited[x][y] = True
    lists = deque()

    # 상좌우하
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    
    # 현재 위치 x,y 기준 최단거리 테이블 board 만들기
    while queue:
        ax,bx = queue.popleft()
        for i in range(4):
            nx,ny = ax+dx[i], bx+dy[i]
            
            if nx >=0 and ny>=0 and nx<n and ny<n and not visited[nx][ny] and mat[nx][ny] <= size:
                queue.append((nx,ny))
                visited[nx][ny] = True
                board[nx][ny] = board[ax][bx] + 1   

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and mat[i][j] != 0 and mat[i][j] < size:
                lists.append((board[i][j],i,j))
    lists = sorted(lists) 
    return lists

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            # 초기 위치 설정
            x,y = i,j   
            matrix[i][j] = 0 

while True:
    # lst는 현재위치에서 물고기들의 거리 리스트
    lst = deque(go(matrix,x,y))
    # print(lst)

    if len(lst) == 0:
        break

    f,a,b = lst.popleft()

    second += f
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
 
    matrix[a][b] = 0
    x,y = a,b

print(second)