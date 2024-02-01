# 위상 정렬 사용
# 올해 순위 1등부터 출력 (위상 정렬 결과가 여러개면 "?", 사이클 발생하면 "IMPOSSIBLE" 출력)
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 팀의 총 개수
    n = int(input())
    # 작년에 i등을 한 팀 ti의 번호 (1 <= i)
    last_year = list(map(int,input().split()))
    # 그래프 선언
    graph = [[False] * (n+1) for _ in range(n+1)]
    # 진입 차수, 숫자가 낮을수록 순위가 높다
    indegree = [0 for _ in range(n+1)]
    
    for i in range(n):
        for j in range(i+1,n):
            graph[last_year[i]][last_year[j]] = True
            # j의 진입차수 += 1
            indegree[last_year[j]] += 1

    # 순위가 바뀐 팀의 개수
    m = int(input())
    # 상대적 등수가 바뀐 두 팀 a,b
    for _ in range(m):
        a,b = map(int,input().split())

        # 상대적 순위가 바뀐다는 건 graph의 방향을 뒤집는 것
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬 함수
    result = []
    q = deque()

    # 진입 차수가 0이면 전부 큐에 넣는다
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i) 
    
    cycle = False
    One = True

    for i in range(n):
        # 큐가 비어있으면 사이클 발생
        if len(q) == 0:
            cycle = True
            break
        # 결과가 여러개
        if len(q) >= 2:
            One = False
            break

        # 현재 노드 now
        now = q.popleft()
        result.append(now)

        for j in range(1,n+1):
            # 현재 노드에 연결되어 있는 모든 노드의 위상정렬 - 1, 값이 0이되면 큐에 넣기
            if graph[now][j]:
                indegree[j] -=1
                if indegree[j] == 0:
                    q.append(j)
    
    if cycle:
        print("IMPOSSIBLE")
    elif not One:
        print("?")
    else:
        print(*result)
    

    