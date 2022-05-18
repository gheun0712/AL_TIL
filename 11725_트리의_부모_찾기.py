# 11725_트리의_부모_찾기
# 2022-05-18

import sys
input = sys.stdin.readline

node = int(input())
node_graph = [[] for _ in range(node + 1)]
parent = [[] for _ in range(node + 1)]

# 트리를 그래프 형태로 생성

for _ in range(node - 1):
    i, j = map(int, input().split())
    node_graph[i].append(j)
    node_graph[j].append(i)


def dfs(graph_list, start, parent):
    stack = [start]

    while stack:
        node = stack.pop()
        for i in graph_list[node]:
            parent[i].append(node)
            stack.append(i)
            graph_list[i].remove(node)
    return parent


for i in list(dfs(node_graph, 1, parent))[2:]:
    print(i[0])
