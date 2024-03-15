import pprint
import copy
matrix = []
ans = 0
for _ in range(4):
    a1,b1,a2,b2,a3,b3,a4,b4 = map(int,input().split())
    matrix.append([[a1,b1-1],[a2,b2-1],[a3,b3-1],[a4,b4-1]])

# 방향 반환
def get_dir(num,x,y):
    dir = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
    return dir[num][0],dir[num][1]

# 물고기 움직이기
def move_fish(mat,sx,sy):
    for n in range(1,17):
        is_in = False
        x,y = 0,0
        for i in range(4):
            for j in range(4):
                if mat[i][j][0] == n: 
                    x,y = i,j
                    is_in = True

        if is_in:
            dir = mat[x][y][1]
            for _ in range(8):
                a,b = get_dir(dir,x,y)
                nx,ny = x+a,y+b
                if nx >= 0 and ny >= 0 and nx < 4 and ny <4 :
                    # 상어가 없으면 45도 회전
                    if not (nx == sx and ny == sy):
                        mat[x][y][1] = dir 
                        mat[nx][ny],mat[x][y]= mat[x][y],mat[nx][ny]     
                        break  
                dir = (dir+1)%8   
    return mat

# x,y 좌표에 있는 상어가 먹을 수 있는 물고기의 좌표 lst 반환
def can_shark_eat(mat,x,y):
    lst = []
    i,j = get_dir(mat[x][y][1],x,y)
    for _ in range(3):
        x,y = x+i,y+j
        if x >= 0 and y >= 0 and x < 4 and y <4 and mat[x][y][0] != -1:
            lst.append([x,y])
    return lst

def dfs(mat,eat,x,y):
    global ans
    graph = copy.deepcopy(mat)
    eat += graph[x][y][0]
    graph[x][y][0] = -1
    move_fish(graph,x,y)
    lst = can_shark_eat(graph,x,y)

    if lst:
        for nx,ny in lst:
            dfs(graph,eat,nx,ny)
    else:
        ans = max(ans,eat)
        return
           
ans = 0
dfs(matrix,0,0,0)
print(ans)


