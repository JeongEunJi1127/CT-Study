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

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

for i in range(n):
    lst = list(map(int,input().split()))
    for j in range(n):
        if lst[j] == 1:
            union_parent(parent,i+1,j+1)

plan = list(map(int,input().split()))
ans = True

for i in range(m-1):
    if find_parent(parent,plan[i]) != find_parent(parent,plan[i+1]):
        ans = False

if ans:
    print("YES")
else:
    print("NO")