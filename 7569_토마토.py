# 7569_토마토
# 2022-03-20

from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
cnt = 0

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 0, 1, 0]
dy = [0, 0, 0, -1, 0, 1]

q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append((i, j, k, 0))

while q:
    z, x, y, cnt = q.popleft()

    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        c = cnt + 1

        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = 1
                q.append((nz, nx, ny, c))

for i in range(H):
    for j in range(N):
        if box[i][j].count(0) > 0:
            cnt = -1
            break

print(cnt)
