# 5014_스타트링크
# 22-03-20

from collections import deque


def BFS():
    q = deque()
    visited[s-1] = 1
    q.append(s-1)

    while q:
        floor = q.popleft()
        for i in range(2):
            nf = floor + direction[i]

            if 0 <= nf < f and visited[nf] == 0:
                res[nf] = res[floor] + 1
                q.append(nf)
                visited[nf] = 1


f, s, g, u, d = map(int, input().split())

visited = [0] * (f+1)
res = [-1] * (f+1)
# 현재 위치
res[s-1] = 0
# 위층, 아래층 위치 저장
direction = [u, -d]

BFS()

print(res[g-1] if res[g-1] != -1 else "use the stairs")