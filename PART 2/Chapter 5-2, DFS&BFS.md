## `Chapter 5` DFS/BFS

### :three: 음료수 얼려 먹기
> N*M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 

:speech_balloon: 특정 지점의 주변 상하좌우를 탐색하고 방문하지 않은 지점이 있다면 방문, 문한 지점에서 다시 상하좌우를 탐색하며 연결된 모든 지점을 센다.    
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%205%20DFS%26BFS/%EC%9D%8C%EB%A3%8C%EC%88%98%20%EC%96%BC%EB%A0%A4%20%EB%A8%B9%EA%B8%B0.py)

### :four: 미로 탈출
> N*M 크기의 미로에 동빈이의 위치는 (1,1) 이고, 미로의 출구는 (N,M)에 존재하며 한 번에 한 칸씩 이동할 수 있다. 괴물이 있는 부분은 0, 있는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

:speech_balloon: 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하므로 BFS를 활용하여 문제를 해결할 수 있다.  
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%205%20DFS%26BFS/%EB%AF%B8%EB%A1%9C%20%ED%83%88%EC%B6%9C.py)