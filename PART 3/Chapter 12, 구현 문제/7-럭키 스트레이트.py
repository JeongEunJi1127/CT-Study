n = list(input())

def lucky_stright(num):
    # 왼쪽 부분인지 오른쪽 부분인지 구분할 기준 
    standard = len(num)//2
    left = 0
    right = 0
    for i in range(len(num)):
        # 기준보다 왼쪽이면 left에 현재 정수 더하기
        if i < standard:
            left += int(num[i])
        # 기준보다 오른쪽이면 right에 현재 정수 더하기
        else:
            right += int(num[i])
    if left == right:
        print("LUCKY")
    else:
        print("READY")

lucky_stright(n)