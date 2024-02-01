# 탑승구(노드) 수
g = int(input())
# 비행기(간선) 수
p = int(input())
parent = [i for i in range(g+1)]

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

cnt = 0

for i in range(1,p+1):
    # i번째 비행기가 도킹하는 탑승구의 위치 1~n
    n = int(input())
    root = find_parent(parent,n)

    # 도킹할 수 없으면 즉시 중지
    if root==0:
        break

    # 탑승구 최대 번호에 도킹하고, -1만큼 작은 탑승구를 root로
    union_parent(parent, root, root-1)
    cnt += 1

print(cnt)