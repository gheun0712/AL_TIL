# 15684_사다리_조작
# 2022-04-13
# 2022-04-18

"""
check 리스트를 통해서 주어진 정보에서 현재 존재하고 있는 사다리 지점을 표시
사다리가 양 옆으로는 추가로 연결할 수 없기 때문에 check 표시 안된 곳을 구하기
그리고 이를 data 리스트에 추가해줘서 정보 저장해주기!

DFS를 통해서 기본 탐색하도록 설정하기
i = i 로 도착하도록 확인하는 check 함수 만들어주기
>> check 리스트명을 visited로 안 겹치게 바꿔주기
결과에서 3보다 크면 -1을 출력해야하므로 미리 3보다 큰 4로 설정해서 비교해주기
"""


def check():
    for i in range(1, n + 1):
        now = i
        for j in range(1, h + 1):
            if visited[j][now - 1]:
                now -= 1
            elif visited[j][now]:
                now += 1
        if now != i:
            return 0
    return 1


def dfs(depth, idx):
    global res
    if depth >= res:
        return
    if check():
        res = depth
        return

    for c in range(idx, len(data)):
        x, y = data[c]
        if not visited[x][y - 1] and not visited[x][y + 1]:
            visited[x][y] = 1
            dfs(depth + 1, c + 1)
            visited[x][y] = 0


n, m, h = map(int, input().split())
visited = [[0] * (n + 1) for _ in range(h + 1)]
data = []
for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = 1

for i in range(1, h + 1):
    for j in range(1, n):
        if not visited[i][j - 1] and not visited[i][j] and not visited[i][j + 1]:
            data.append([i, j])

res = 4
dfs(0, 0)

print(res) if res < 4 else print(-1)

