# 2468_안전영역
# 2022-03-19

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1


N = int(input())
num_lst = [list(map(int, input().split())) for _ in range(N)]
res = []

for i in range(101):
    visited = [[0] * N for i in range(N)]
    cnt = 0
    # 침수되는 영역은 1로 숫자 바꿔주기
    for j in range(N):
        for k in range(N):
            if num_lst[j][k] <= i:
                visited[j][k] = 1
    # BFS 탐색 후에 카운트 올려주기
    for j in range(N):
        for k in range(N):
            if visited[j][k] == 0:
                BFS(j, k)
                cnt += 1

    res.append(cnt)

print(max(res))
