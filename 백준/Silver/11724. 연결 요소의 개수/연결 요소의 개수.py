from collections import deque


def BFS(start):
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()

        for j in lst[node]:
            if not visited[j]:
                visited[j] = True
                q.append(j)


N, M = map(int, input().split())
# 그래프 만들 그래프 만들기
lst = [[] for _ in range(N + 1)]
# 점들 기준 인덱스에 각각 도착점 넣어주기
for _ in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
    
# 방문 체크 리스트
visited = [False] * (N + 1)
# 형성되는 독립 그래프 갯수
cnt = 0

# N개까지 무조건 하나의 선은 존재하기 때문에 모두 체크해주기
for num in range(1, N + 1):
    if not visited[num]:
        # 연결되는 그래프 없을 시에는 카운트 +1
        if not lst[num]:
            cnt += 1
            visited[num] = True
            
        # 아직 방문하지 않았고, 연결되는 지점이 있는 경우
        else:
            BFS(num)
            cnt += 1

print(cnt)
