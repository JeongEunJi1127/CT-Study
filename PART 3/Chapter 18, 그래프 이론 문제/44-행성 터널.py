# 크루스칼 알고리즘
# 간선의 개수 = 노드의 개수 -1
# 최소 비용의 신장 트리 구할 때 사용
import sys
input = sys.stdin.readline
n = int(input())
parent = [i for i in range(n+1)]

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

xlst = []
ylst = []
zlst = []

for i in range(1,n+1):
    x,y,z = map(int,input().split())
    xlst.append((x,i))
    ylst.append((y,i))
    zlst.append((z,i))

# 비용이 가장 작은 간선이 선택 -> x, y, z 상관없이 정렬하여 인접한 점 사이 간선의 길이만 구하면 된다
xlst.sort()
ylst.sort()
zlst.sort()

lst = []
for i in range(n-1):
    # 두 점사이 거리, 앞의 점, 뒤의 점
    lst.append((xlst[i+1][0] - xlst[i][0], xlst[i+1][1], xlst[i][1]))
    lst.append((ylst[i+1][0] - ylst[i][0], ylst[i+1][1], ylst[i][1]))
    lst.append((zlst[i+1][0] - zlst[i][0], zlst[i+1][1], zlst[i][1]))

lst.sort()

ans = 0
for i in lst:
    cost, a, b = i
    # 사이클이 존재하지 않으면 합치기
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans += cost
print(ans)