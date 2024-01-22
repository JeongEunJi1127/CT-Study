# 0~9로 이루어진 문자열 s
s = input()
# 정답 변수 
ans = int(s[0])

for i in range(len(s)-1):
    # num을 정수로 변환
    num = int(s[i])
    # num이 0또는 1이면 더하기
    if num == 0 or num == 1:
        ans += int(s[i+1])
    # num이 2~9면 곱하기
    else: 
        ans *= int(s[i+1])
print(ans)


