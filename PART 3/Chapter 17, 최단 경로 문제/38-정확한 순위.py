n,m = map(int,input().split())
lst = [[int(1e9) for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    # a가 b보다 작음
    a,b = map(int,input().split())
    lst[a][b] = 1

# 자기 자신으로 가는 경우 0    
for i in range(n):
    lst[i][i] = 0

# 플로이드 워
for i in range(1,n+1):
    for j in range(1,n+1): 
        for k in range(1,n+1):
            lst[j][k] = min(lst[j][k], lst[j][i] + lst[i][k])
ans = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if lst[i][j] != int(1e9) or lst[j][i] != int(1e9):
            cnt+=1
    if cnt == n:
        ans+=1

print(ans)