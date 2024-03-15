import copy
import sys
from collections import deque
input = sys.stdin.readline

n,l,r = map(int,input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

# 1. 인구 이동이 발생하는지 확인하는 함수
def can_move(i,j):
    if abs(i-j) >= l and abs(i-j) <= r:
        return True
    else:
        return False

# 2. 인구 이동 함수 
def move_population(matrix,lst):
    sums = 0
    for i in lst:
        sums += matrix[i[0]][i[1]]
    sums //= len(lst)
    for i in lst:
        matrix[i[0]][i[1]] = sums
    return matrix

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 3. bfs 탐색을 통해 인구 이동이 가능한 국가들 탐색
def bfs(a,b,visited):
    # 연합 국가 저장할 리스트 lst
    lst = set()
    queue = deque([(a,b)])
    visited[a][b] = True
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if nx>=0 and ny>=0 and nx<n and ny<n:
                if not visited[nx][ny] and can_move(matrix[x][y],matrix[nx][ny]):
                    lst.add((x,y))
                    lst.add((nx,ny))
                    queue.append((nx,ny))
                    visited[nx][ny] = True
    return lst

cnt = 0
while True:
    mat = copy.deepcopy(matrix)
    moved = False
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            lst = list(bfs(i,j,visited))
            if len(lst) != 0:
                moved = True
                move_population(mat,lst)
    matrix = mat
    if moved: cnt += 1
    else: break
print(cnt)
