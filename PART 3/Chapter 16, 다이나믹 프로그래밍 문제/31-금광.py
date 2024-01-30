t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    matrix = []

    # 배열 모양 만들기
    for i in range(0,len(lst),m):
        matrix.append(lst[i:i+m])

    for i in range(1,m):
        for j in range(n):
            # 왼쪽이나 왼쪽 밑에서 올 수있다
            if j == 0:
                up_left = 0
            else:
                up_left = matrix[j-1][i-1]
            # 왼쪽이나 왼쪽 위에서 올 수 있다
            if j == n-1:
                down_left = 0
            else:
                down_left =  matrix[j+1][i-1]
            left = matrix[j][i-1]
            # 점화식
            matrix[j][i] = matrix[j][i] + max(left,up_left,down_left)
    ans = 0

    for i in range(n):
        ans = max(ans,matrix[i][m-1])
    print(ans)
            
        
            


    