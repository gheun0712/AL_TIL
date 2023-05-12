from collections import deque


def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 색깔이 같은 영역 구분하기
                if lst[nx][ny] == lst[x][y]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


n = int(input())
lst = [list(map(str, input())) for _ in range(n)]
ans1 = 0
ans2 = 0

# 정상인일 때 카운트
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            ans1 += 1

# 색약일 때 카운트
visited = [[0] * n for _ in range(n)]

# 빨간색 초록색 구분 안되기 때문에 하나의 색으로 만들어주기
for i in range(n):
    for j in range(n):
        if lst[i][j] == 'G':
            lst[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            ans2 += 1

print(ans1, ans2)
