from collections import Counter
# 볼링공의 개수 n, 공의 최대 무게의 개수 m
n,m = map(int,input().split())
# 각 공의 무게
weights = list(map(int,input().split()))
# 경우의 수 저장할 변수
ans = 0
# lst에 counter 라이브러리를 이용하여 공의 무게 별 개수 정리 
lst = Counter(weights).most_common()

while lst: 
    k = 0
    # 리스트의 길이가 1이면 종료
    if len(lst) <= 1:
        break
    # 1번째 인덱스부터의 최대 무게 개수 k에 더하기
    for i in lst[1:]:
        k+=i[1]
    # 0번째 인덱스 무게의 개수 * 나머지 무게의 개수
    ans += lst[0][1] * k
    # 리스트의 0번째 인덱스 삭제
    lst = lst[1:]
print(ans)
