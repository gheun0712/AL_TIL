import sys

sys.setrecursionlimit(100000)


def DFS(x, y):
    global temp
    lst[x][y] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and not lst[nx][ny]:
            # 넓이 계산해주기
            temp += 1
            DFS(nx, ny)


m, n, k = map(int, input().split())
lst = [[0] * n for _ in range(m)]
# 넓이 카운트 해 줄 변수
temp = 1
# 영역 개수
cnt = 0
# 넓이 오름차순 정리해서 출력해주기
ans = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            lst[i][j] = 1

for a in range(m):
    for b in range(n):
        if not lst[a][b]:
            cnt += 1
            DFS(a, b)
            # 계산한 넓이 입력해주고 변수 초기화
            ans.append(temp)
            temp = 1

ans.sort()
print(cnt)
print(' '.join(map(str, ans)))
