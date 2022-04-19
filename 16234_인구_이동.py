# 16234_인구_이동
# 2022-04-20

"""
L이상 R명 이하 일때 국경 개방
국경 개방 되면 (개방된 곳 합 / 개방된 곳 갯수) >> 소수점 버림
탐색해서 인접한 칸의 조건이 맞다면 계산해주기
BFS로 구현해줄까아아

pypy3 => 1296ms
"""
import collections


def BFS(i, j):
    q = collections.deque()
    q.append((i, j))
    visited[i][j] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    union = [(i, j, people[i][j])]

    while q:
        x, y = q.popleft()
        population = people[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(people[nx][ny] - population) <= R:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    union.append((nx, ny, people[nx][ny]))

    if len(union) == 1:
        return 0

    total = 0
    for x, y, population in union:
        total += population

    avg = total // len(union)  # 인구 이동
    for x, y, population in union:
        people[x][y] = avg

    return 1


N, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    visited = [[0] * N for _ in range(N)]

    move = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                move += BFS(i, j)

    if move == 0:
        break

    ans += 1

print(ans)