# 2644_촌수계산(DFS)
# 2022-03-14


def DFS(a):
    global g, visited, p1

    for i in g[a]:
        if i != p1 and visited[i] == 0:
            visited[i] = visited[a] + 1
            DFS(i)


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
g = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

DFS(p1)

if visited[p2] == 0:
    print(-1)

else:
    print(visited[p2])
