from collections import deque


def BFS(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    dx = [0, 0, 1, -1, 1, -1, 1, -1]
    dy = [1, -1, 0, 0, 1, -1, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and g[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    g = []
    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for _ in range(h):
        g.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if g[i][j] == 1 and not visited[i][j]:
                BFS(i, j)
                cnt += 1

    print(cnt)
