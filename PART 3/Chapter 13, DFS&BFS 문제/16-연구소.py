from itertools import combinations
import copy
n,m = map(int,input().split())
matrix = []
ans = 0

for _ in range(n):
    matrix.append(list(map(int,input().split())))

# bfs 이용하여 바이러스 퍼뜨리기
def spread_virus(matrix):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    idx = copy.deepcopy(idx2)
    while idx:
        i,j = idx.pop()
        for k in range(4):
            x,y = i+dx[k],j+dy[k]
            if x<0 or x>=n or y<0 or y>=m:
                continue
            elif matrix[x][y] == 0:
                matrix[x][y] = 2
                idx.add((x,y))
    return matrix

idx0 = set()
idx2 = set()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            idx0.add((i,j))
        elif matrix[i][j] == 2:
            idx2.add((i,j))

#idx0 에서 3개를 1로 바꾼후 spread_virus 실행, 0의 개수 세기
select3_idx0 = list(combinations(idx0,3))
sample = []
for i in select3_idx0:
    sample = copy.deepcopy(matrix)
    for j in i:
        sample[j[0]][j[1]] = 1
    sample_lst = spread_virus(sample)
    cnt = 0
    for i in sample_lst:
        cnt += i.count(0)
    ans = max(ans,cnt)

print(ans)