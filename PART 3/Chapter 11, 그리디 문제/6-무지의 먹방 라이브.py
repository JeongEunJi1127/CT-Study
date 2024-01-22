# k값이 충분하다면 음식을 다 먹는데 드는 시간이 가장 적은 것부터 처리 ->  heapq 자료구조 사용
import heapq
def solution(food_times, k):
    # 모든 음식을 먹는 데에 시간이 충분하지 않으면 -1 리턴
    if sum(food_times) <= k:
        return -1
    q = []
    # q에 (음식을 먹는데 드는 시간, 음식의 번호) 삽입
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    print(q)
    # 먹기 위해 사용한 시간
    sum_value = 0
    # 직전 음식 시간
    prev = 0
    # 남은 음식의 개수
    length = len(food_times)
    
    while sum_value + ((q[0][0] - prev)) <= k:
        # now는 현재 음식을 먹는데 드는 시간
        now = heapq.heappop(q)[0]
        sum_value += (now - prev) * length
        length -= 1 # 다 먹은 음식 제외
        prev = now # 이전 음식 시간 재설정
    # 결과를 음식의 번호 기준으로 정렬
    result = sorted(q,key = lambda x:x[1])
    return result[(k-sum_value) % length][1]
