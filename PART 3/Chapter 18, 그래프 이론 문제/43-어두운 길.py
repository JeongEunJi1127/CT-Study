n,m = map(int,input().split())
parent = [i for i in range(1,n+1)]

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

lst = []

for _ in range(m):
    x,y,z = map(int,input().split())
    lst.append((z,x,y))

# 전체 가로등 비용
cnt = 0 
ans = 0

for i in lst :
  cost, a, b = i
  cnt += cost
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b) :
    union_parent(parent, a, b)
    ans += cost

print(cnt - ans)