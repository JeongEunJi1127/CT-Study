n = int(input())
battle_power = list(map(int,input().split()))
# 오름차순으로 정렬
battle_power = battle_power[::-1]
dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        # 앞의 수 battle_power[j]보다 뒤의 수 battle_power[i]가 크면 
        if battle_power[j] < battle_power[i]:
            # 기존 경로 dp[i]를 통한 경우의 수와 그 전 경로 dp[j]에 1을 더한 경우의 수 중 큰 값으로 갱신
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))