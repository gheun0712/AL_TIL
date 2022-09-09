# 9205_맥주 마시면서 걸어가기(BFS)
# 22-03-19

from collections import deque


def BFS(x):
    q = deque()
    q.append(0)

    while q:
        x = q.popleft()
        for i in range(n + 2):
            if g[x][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n + 2)]
    g = [[0] * (n + 2) for _ in range(n + 2)]
    visited = [0] * (n + 2)

    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                continue
            # 2차원 행렬로 리스트 만들어서 연결시켜주기
            if abs(lst[i][0] - lst[j][0]) + abs(lst[i][1] - lst[j][1]) <= 1000:
                g[i][j] = 1
                g[j][i] = 1

    visited[0] = 1
    BFS(0)
    print("happy" if visited[-1] else "sad")
