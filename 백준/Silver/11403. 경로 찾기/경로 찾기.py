from collections import deque
import sys

input = sys.stdin.readline

def BFS(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if lst[q][i] == 1 and check[i] == 0:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    BFS(i)

for j in visited:
    print(*j)
