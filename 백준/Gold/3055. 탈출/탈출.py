from collections import deque
import sys

input = sys.stdin.readline


# 물이 차있는 지역 탐색
def find():
    q_len = len(water)

    while q_len:
        x, y = water.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and maps[nx][ny] == ".":
                maps[nx][ny] = "*"
                water.append([nx, ny])

        q_len -= 1


# 고슴도치 이동 탐색
def BFS(x, y):
    q.append([x, y])
    visited[x][y] = 1

    while q:
        q_len = len(q)

        while q_len:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C:

                    if maps[nx][ny] == "." and not visited[nx][ny]:
                        q.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1

                    elif maps[nx][ny] == "D":
                        print(visited[x][y])
                        return

            q_len -= 1

        find()

    print("KAKTUS")
    return


R, C = map(int, input().split())
maps = [list(map(str, input().strip())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

q = deque()
water = deque()

dx = [0, 0, 1, -1]
dy = [1, - 1, 0, 0]

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'S':
            a, b = i, j
            maps[i][j] = '.'

        elif maps[i][j] == '*':
            water.append([i, j])

find()
BFS(a, b)
