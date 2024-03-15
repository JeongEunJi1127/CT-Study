from collections import deque

# bfs 사용
def solution(board):
    # 보드의 길이
    n = len(board)
    # 아래, 오른쪽, 위, 왼쪽
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    # 행, 열, 방향, 이동횟수 (방향은 가로 1, 세로 0 으로 두자)
    queue = deque([(0,0,1,0)])
    # 행, 열, 방향
    visited = set([0,0,1])

    while queue:
        x1, y1, rdir, moves = queue.popleft()
        x2, y2 = x1 + directions[rdir][0], y1 + directions[rdir][1]
        # (n,n) 에 도착
        if x2 == n-1 and y2 == n-1: 
            return moves

        for i in range(4):
            nx1, ny1 = x1 + directions[i][0], y1 + directions[i][1]
            nx2, ny2 = x2 + directions[i][0], y2 + directions[i][1]

            # 보드 벗어나면 이동하지 않는다
            if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0 <=ny2<n:
                if (nx1, ny1, rdir) in visited or board[nx1][ny1] == 1 or board[nx2][ny2] == 1:
                    continue

                # 보드 내에 있으면 현재 방향에서 상하좌우로 이동
                queue.append((nx1,ny1,rdir,moves+1))
                visited.add((nx1,ny1,rdir))

                # 방향 회전 (xor 연산자 ^ 사용)
                dirs = rdir ^ 1

                # 로봇 세로 + 오른쪽으로 회전, 로봇 가로 + 아래쪽으로 회전
                if rdir + i == 1:
                    if (x1, y1, dirs) not in visited:
                        queue.append((x1, y1, dirs, moves + 1))
                        visited.add((x1, y1, dirs))
                    if (x2, y2, dirs) not in visited:
                        queue.append((x2, y2, dirs, moves + 1))
                        visited.add((x2, y2, dirs))
                # 로봇 세로 + 왼쪽으로 회전, 로봇 가로 + 위쪽으로 회전
                elif rdir + i == 3:
                    if (nx1, ny1, dirs) not in visited:
                        queue.append((nx1, ny1, dirs, moves + 1))
                        visited.add((nx1, ny1, dirs))
                    if (nx2, ny2, dirs) not in visited:
                        queue.append((nx2, ny2, dirs, moves + 1))
                        visited.add((nx2, ny2, dirs))
    return -1

# 7
print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))