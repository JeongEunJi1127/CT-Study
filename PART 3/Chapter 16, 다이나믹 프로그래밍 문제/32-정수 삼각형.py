n = int(input())
# 바로 위나 바로 왼쪽 위의 숫자로만 이동할 수 있다.
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j])
triangle = []
for _ in range(n):
    triangle.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = triangle[i-1][j-1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = triangle[i-1][j]

        triangle[i][j] = triangle[i][j] + max(up,up_left)
# 마지막 줄의 숫자 중 가장 큰 수가 최대 경로
print(max(triangle[n-1]))