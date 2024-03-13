from itertools import combinations
import copy

n = int(input())
matrix = []
for _ in range(n): 
    matrix.append(list(map(str,input().split())))
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def get_pos(p):
    pos = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == p:
                pos.append((i,j))
    return pos

# 학생 찾으면 true
def find_student(matrix):
    # 선생의 위치 pos에 저장
    pos = get_pos("T")
    # 모든 pos에 대해, 상하좌우로 한줄씩 탐색
    for i in pos:
        x,y = i[0], i[1]
        for j in range(4):
            nx,ny = x,y
            while True:
                nx,ny = nx+dx[j],ny+dy[j]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    break
                elif matrix[nx][ny] == "O":
                    break
                # 학생이 보이면 이 matrix는 모든 학생을 숨기는 데에 실패한 matrix이므로 false 리턴
                elif matrix[nx][ny] == "S":
                    return True
    return False

posx = list(combinations(get_pos("X"),3))
can=False
for i in posx:
    x,y,z = i
    mat = copy.deepcopy(matrix)
    mat[x[0]][x[1]] = "O"
    mat[y[0]][y[1]] = "O"
    mat[z[0]][z[1]] = "O"

    if not find_student(mat):
        can = True
if can:
    print("YES")
else:
    print("NO")