import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards,int(input()))
ans = 0

while len(cards)>1:
    sum_cards = heapq.heappop(cards)+heapq.heappop(cards)
    ans+=sum_cards
    heapq.heappush(cards,sum_cards)
    
print(ans)
    