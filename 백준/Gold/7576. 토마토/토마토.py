import sys
from collections import deque

input = sys.stdin.readline


def BFS():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 토마토 익지 않은 부분 익혀주고, +1 해주면서 일수 카운트 올려주기
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append([nx, ny])


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
ans = 0
flag = False
q = deque()

for i in range(n):
    for j in range(m):
        # 익은 토마토가 여러개인 경우를 위해서 q에 넣어두고 bfs 탐색하기
        if tomato[i][j] == 1:
            q.append([i, j])

BFS()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            flag = True
            break
        ans = max(ans, tomato[i][j])

if flag:
    print(-1)
elif ans == -1:
    print(0)
else:
    print(ans - 1)
