# 1916_최소비용_구하기
# 2022-05-10

"""
최소비용이니깐 다익스트라 알고리즘을 사용해보자!
"""
import heapq

N = int(input())
M = int(input())
info = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    info[a].append((b, w))

start, end = map(int, input().split())
INF = int(1e9)
distance = [INF] * (N + 1)


def dijkstra(st):
    distance[st] = 0
    q = [(0, start)]

    while q:
        w, now = heapq.heappop(q)

        if distance[now] < w:
            continue

        for destination, weight in info[now]:
            cost = distance[now] + weight
            if distance[destination] > cost:
                distance[destination] = cost
                heapq.heappush(q, (cost, destination))


dijkstra(start)
print(distance[end])
