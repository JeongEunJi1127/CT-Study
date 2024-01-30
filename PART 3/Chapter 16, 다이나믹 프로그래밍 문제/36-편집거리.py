# 문자열 a를 문자열 b로 바꾸는 최소 연산 횟수를 구하여라
a = list(input())
b = list(input())
# 최소 연산 거리를 담을 2차원 배열 선언
dp = [[0 for i in range(len(b)+1)] for _ in range(len(a)+1)]

# dp 테이블 초기 설정
for i in range(1,len(a)+1):
    dp[i][0] = i
for j in range(1,len(b)+1):
    dp[0][j] = j

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        # 글자가 같으면 dp[i][j] == dp[i-1][j-1]
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        # 글자가 다르면 1 + min(삭제,삽입,교체)
        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[len(a)][len(b)])