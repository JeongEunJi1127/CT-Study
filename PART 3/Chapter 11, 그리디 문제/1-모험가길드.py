# 모험가 n명
n = int(input())

# 모험가 n명의 공포도 x 리스트
fears = list(map(int,input().split()))

# 공포도가 x인 모험가는 반드시 x명 이상으로 구성된 모험가 그룹에 참가해야함 -> 공포도가 낮은 여행자 먼저 그룹을 만들자
# sort를 이용해 공포도 오름차순 정렬
fears.sort()

# 그룹의 개수 
ans = 0
# 현재 모험가의 수
cnt = 0

for i in fears:
    # 현재 그룹에 있는 모험가의 개수 1 더하기
    cnt += 1
    # 만약 현자 공포도보다 모험가의 수가 같거나 많으면
    if cnt >= i:
        # 그룹 결성
        ans+=1
        # 모험가의 수 초기화
        cnt=0

print(ans)
    
