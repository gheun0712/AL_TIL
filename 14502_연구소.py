# 14502_연구소
# 2022-03-31

# 먼저, DFS로 울타리 설치 탐색부터 돌리고
# 울타리 설치후에 울타리 안에 바이러스 퍼뜨려주고
# 남은 0 ( 안전영역 ) count


def dfs(cnt):
    global ans

    # 울타리 3개 다 세웠으면 바이러스 퍼뜨리러 가야지~
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                visited[i][j] = maps[i][j]

        for i in range(n):
            for j in range(m):
                if visited[i][j] == 2:
                    virus(i, j)

        ans = max(ans, safe())
        return

    # 울타리 공사 시작
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                cnt += 1
                dfs(cnt)
                # 초기화 해줘야지
                maps[i][j] = 0
                cnt -= 1


# 본격 바이러스 퍼뜨리기 대작전
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 2
                virus(nx, ny)
    return


# 0만 남은곳 찾아서 안전영역 카운팅 해주기
def safe():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                cnt += 1

    return cnt


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
ans = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dfs(0)

print(ans)
