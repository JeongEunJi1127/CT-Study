import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(input().split())
lst.sort(key = lambda x:((-1)*int(x[1]),int(x[2]),(-1)*int(x[3]),x[0]))

for i in lst:
    print(i[0])