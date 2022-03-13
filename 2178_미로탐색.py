# 2178_미로탐색
# 2022-03-13

from collections import deque


def BFS(a, b):
    q = deque()
    q.append((a, b))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1:
                q.append((nx, ny))
                g[nx][ny] = g[x][y] + 1


n, m = map(int, input().split())
g = []

for _ in range(n):
    g.append(list(map(int, input())))

BFS(0, 0)
print(g[n - 1][m - 1])
