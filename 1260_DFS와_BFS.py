# 1260_DFS와_BFS
# 2022-03-12

from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# n : 정점 개수, m : 간선 개수, v : 탐색 시작 정점 번호
n, m, v = map(int, input().split())
# 리스트는 1부터이니까 하나 더 추가!
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # 간선 m개 정보 받기
    temp_list = list(map(int, input().split()))
    # 시작과 끝 저장하기
    graph[temp_list[0]].append(temp_list[1])
    graph[temp_list[1]].append(temp_list[0])

for i in range(n + 1):
    graph[i].sort()

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)
