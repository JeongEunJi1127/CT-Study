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