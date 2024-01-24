s = input()
ans = []
cnt = 0

for i in s:
    if i.isdigit():
        cnt += int(i)
    elif i.isalpha():
        ans.append(i)
ans.sort()
ans.append(str(cnt))

for i in ans:
    print(i,end="")