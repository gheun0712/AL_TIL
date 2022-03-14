# 1697_숨바꼭질(BFS)
# 2022-03-14
from collections import deque


def BFS():
    q = deque()
    q.append(n)

    while q:
        sister = q.popleft()
        if sister == k:
            return
        for i in (sister - 1, sister + 1, sister * 2):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[sister] + 1
                q.append(i)


n, k = map(int, input().split())
visited = [0] * 100001

BFS()
print(visited[k])
