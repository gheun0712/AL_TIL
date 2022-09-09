# 14500_테트로미노
# 2022-03-30

# 총 4칸으로 구성된 도형
# 각 도형 모형대로 구현 > 시간 초과 뜰거 같음
# 4칸이니까 4방향 탐색으로 구현해보자
# 근데 'ㅗ' 이 모양은 어떻게 구현해내야 할 지 모르겠네
# 블록별 방향을 x,y 축으로 설정 해줘야 하나
# 에라 모르겠다 그냥 저 방향만 뺴줘서 탐색해보지 뭐 눈누

def dfs(x, y, depth, num):
    global res

    if depth == 4:
        res = max(res, num)
        return

    if num + 1000 * (4 - depth) < res:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, num + nums[nx][ny])
            visited[nx][ny] = False

    return res


def middle(x, y):
    global res

    for i in mf:
        try:
            num = nums[x][y] + nums[x + i[0][0]][y + i[0][1]] + \
                  nums[x + i[1][0]][y + i[1][1]] + nums[x + i[2][0]][y + i[2][1]]
        except:
            num = 0

        res = max(res, num)


N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
res = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

mf = [[(0, 1), (0, 2), (1, 1)], [(0, 1), (0, 2), (-1, 1)],
      [(1, 0), (2, 0), (1, 1)], [(1, 0), (1, -1), (2, 0)]]

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, nums[i][j])
        visited[i][j] = 0
        middle(i, j)

print(res)
