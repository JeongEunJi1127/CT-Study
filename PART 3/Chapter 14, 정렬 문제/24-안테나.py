import sys
input = sys.stdin.readline

n = int(input())
houses = list(map(int,input().split()))
houses.sort()

# 집을 오름차순으로 정렬한 후 그 중간 값이 안테나로부터 집까지의 거리 합이 최소가 되는 조건이다
if n % 2 == 0:
    # 문제 조건에 따라 중간 값 중 더 작은 값을 선택
    mid_index = len(houses)//2 - 1
else: 
    mid_index = len(houses)//2 

print(houses[mid_index])
    