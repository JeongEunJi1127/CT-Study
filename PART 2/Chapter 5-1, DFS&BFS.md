## `Chapter 5` DFS/BFS

### :one: 꼭 필요한 자료구조 기초

#### 탐색
- 많은 양의 데이터 중 원하는 데이터를 찾는 과정
- 그래프, 트리, DFS, BFS

#### 자료구조
- 데이터를 표현하고 관리하고 처리하기 위한 구조
- 오버플로 : 자료구조가 수용할 수 있는 데이터의 크기가 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생
- 언더플로 : 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행할 때 발생

#### 스택
- `선입후출` 또는 `후입선출` 구조
- 파이썬에서는 별도의 라이브러리 없이 append(), pop() 메서드만 이용하면 됨

#### 큐
- `선입선출` 구조
- collections 모듈의 deque 자료구조를 활용하여 구현 가능

#### 재귀 함수
- 자기 자신을 다시 호출하는 함수
- 종료 조건을 명시하여 함수의 무한 호출을 막아야 한다.
- 스택 자료구조 사용 (가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문)

:speech_balloon: 재귀 방식으로 구현한 팩토리얼 예제
```python
def factorial_recursive(n):  
   if n <= 1:  
      return 1  
   return n * factorial_recursive(n-1)
```

:thought_balloon: 수학의 점화식 (특정 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현)을 소스코드로 옮겨 코드가 더 간결함

### :two: 탐색 알고리즘 DFS/BFS

#### 그래프
- 노드(= 정점), 간선으로 표현
- 두 노드가 간선으로 연결되어 있다면 `두 노드는 인접하다` 라고 표현
- 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
- 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식

#### DFS
- 깊이 우선 탐색
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 사용, 재귀 함수 사용

```python
def dfs(graph,v,visited):
   visited[v] = True

   for i in graph[v]:
      if not visited[i]:
         dfs(graph,i,visited)

dfs(graph,1,visited)
```
#### BFS
- 너비 우선 탐색
- 가까운 노드부터 탐색하는 알고리즘
- 큐 사용 -> 수행시간이 DFS보다 좋음 (시간복잡도 O(N))

```python
from collections import deque

def bfs(graph,start,visited):
   queue = deque([start])
   visited[start] = True

   while queue:
      v = queue.popleft()
      for i in graph[v]:
         if not visited[i]:
            queue.append(i)
            visited[i] = True
   
bfs(graph,1,visited)
```

### :three: 음료수 얼려 먹기
> N*M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 

:speech_balloon: 특정 지점의 주변 상하좌우를 탐색하고 방문하지 않은 지점이 있다면 방문, 문한 지점에서 다시 상하좌우를 탐색하며 연결된 모든 지점을 센다.    
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%205%20DFS%26BFS/%EC%9D%8C%EB%A3%8C%EC%88%98%20%EC%96%BC%EB%A0%A4%20%EB%A8%B9%EA%B8%B0.py)

### :four: 미로 탈출
> N*M 크기의 미로에 동빈이의 위치는 (1,1) 이고, 미로의 출구는 (N,M)에 존재하며 한 번에 한 칸씩 이동할 수 있다. 괴물이 있는 부분은 0, 있는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

:speech_balloon: 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하므로 BFS를 활용하여 문제를 해결할 수 있다.  
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%205%20DFS%26BFS/%EB%AF%B8%EB%A1%9C%20%ED%83%88%EC%B6%9C.py)