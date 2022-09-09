# 2667_단지번호붙이기(BFS)
# 2022-03-13

from collections import deque


def BFS(x, y, h):
    q = deque()
    q.append((x, y))
    g[x][y] = 0
    cnt = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] == h and g[nx][ny] != 0:
                    q.append((nx, ny))
                    cnt += 1
                    g[nx][ny] = 0
    return cnt+1


n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, input())))

visited = [[] * n for _ in range(n)]
check_lst = []

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            check_lst.append(BFS(i, j, g[i][j]))

print(len(check_lst))
check_lst.sort()
for k in check_lst:
    print(k)
