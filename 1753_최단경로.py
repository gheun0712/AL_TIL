# 1753_최단경로
# 2022-05-10

"""
최단경로이기 때문에 다익스트라로 풀기!
"""

import heapq
from collections import defaultdict

V, E = map(int, input().split())
start = int(input())
graph = defaultdict(list)
INF = int(1e9)
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node in graph[now]:
            w = dist + node[1]

            if w < distance[node[0]]:
                distance[node[0]] = w
                heapq.heappush(q, (w, node[0]))


dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
