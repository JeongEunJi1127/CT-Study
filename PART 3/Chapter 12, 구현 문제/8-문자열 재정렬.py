s = input()
ans = []
cnt = 0

for i in s:
    # 숫자면 cnt에 더하기
    if i.isdigit():
        cnt += int(i)
    # 문자면 ans에 넣기
    elif i.isalpha():
        ans.append(i)
# 오름차순 정렬
ans.sort()
ans.append(str(cnt))

for i in ans:
    print(i,end="")