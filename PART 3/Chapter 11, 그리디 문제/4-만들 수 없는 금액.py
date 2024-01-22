# 주어진 동전들로 만들 수 없는 양의 정수 금액 중 
# 동전의 개수 n
n = int(input())
# 화폐의 단위
moneys = list(map(int,input().split()))
# moneys를 오름차순으로 정렬
moneys.sort()
# 타겟 값
min_num = 1

for money in moneys:
    # 만들 수 없는 금액을 찾았을 때 종료
    if min_num < money:
        break
    # min_num - 1까지의 모든 금액을 만들 수 있다는 말과 같다
    min_num += money
print(min_num)