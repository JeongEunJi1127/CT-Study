n = int(input())
t = []
p = []
for _ in range(n):
    ti,pi = map(int,input().split())
    t.append(ti)
    p.append(pi)
dp = [0 for _ in range(n+1)]

# 맨 마지막 날부터 탐색
for i in range(n-1,-1,-1):
    # 현재 날짜에서 상담 시작할 때 날짜가 초과되면
    if t[i] + i > n:
        # dp[i]는 지금까지의 상담 최대 금액이다
        dp[i] = dp[i+1]
    # 현재 날짜에서 상담 시작이 가능하면
    else:
        # dp[i]는 (현재 상담 금액 p[i] + 현재 상담을 시작했을 때 끝나는 날의 최대금액 dp[t[i] + i])과 (지금까지의 상담 최대 금액 dp[i+1]) 중 큰 값이다
        dp[i] = max(p[i] + dp[t[i] + i], dp[i+1])
print(dp[0])