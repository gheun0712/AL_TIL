# 2644_촌수계산(BFS)
# 2022-03-14

from collections import deque


def BFS(a):
    q = deque()
    q.append(a)

    while q:
        a = q.popleft()
        for i in g[a]:
            if i != p1 and visited[i] == 0:
                visited[i] = visited[a] + 1
                q.append(i)


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
g = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

BFS(p1)
if visited[p2] == 0:
    print(-1)
else:
    print(visited[p2])
