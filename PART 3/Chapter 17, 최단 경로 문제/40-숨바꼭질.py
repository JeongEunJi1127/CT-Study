import sys
import heapq
input = sys.stdin.readline

n,m = map(int, input().split())
lst = [[] for _ in range(n+1)] 
distance = [int(1e9) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    lst[a].append((b,1))
    lst[b].append((a,1))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in lst[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)
num = max(distance[1:])
print(distance.index(num), num,distance.count(num))