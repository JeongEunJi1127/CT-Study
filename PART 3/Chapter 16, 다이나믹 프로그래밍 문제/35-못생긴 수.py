# 못생긴 수 = 2,3,5만 약수로 가지는 수
n = int(input())
dp = [0 for i in range(n+1)]
dp[1] = 1

# num이 못생긴 수인지 확인
def ugly_num(num):
    while True:
        if num == 1:
            return True
            break
        if num % 2 == 0:
            num //= 2
        elif num % 3 == 0:
            num //= 3
        elif num % 5 == 0:
            num //= 5
        # 2, 3, 5로 나누어지지 않으면 못생긴 수
        else:
            return False

cnt = 2
num = 2

while True:
    if cnt >= n+1:
        break
    # 못생긴 수이면 dp에 저장
    if ugly_num(num):
        dp[cnt] = num
        cnt += 1
    num+=1

print(dp[n])