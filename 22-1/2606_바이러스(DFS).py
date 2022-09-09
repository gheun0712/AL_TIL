# 2606_바이러스(DFS)
# 2022-03-13


def DFS(a):
    if visited[a] == 0:
        visited[a] = 1
        for i in g[a]:
            DFS(i)


n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [0] * (n + 1)
DFS(1)
print(sum(visited) - 1)
