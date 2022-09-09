# 14503_로봇청소기
# 2022-04-03


"""
기본 회전은 dx,dy로 처리하면서 d에 따라서 바라보는 방향에서 왼쪽으로 회전했을때 방향 구하기
처음 있는 곳은 무조건 청소 가능 > cnt + 1
빈 공간이다? > 청소해야지 그렇지 않으면 왼쪽 회전인데 바라보는 방향 기준임
빈 칸은 0 벽은 1이니까 확인한 곳이면 2로 체크하도록 하기

1. 청소가능한지 체크해주고
2. 청소하고
3. 보는 방향에서 왼쪽으로 회전해주기
+) 청소불가이면 후진해줘야함
"""

# def find(x, y, m):
#     global cnt
#
#     while True:
#         for i in range(4):
#             m = (m + 3) % 4
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if arr[nx][ny] == 0:
#                 arr[nx][ny] = 2
#                 cnt += 1
#                 x = nx
#                 y = ny
#                 break
#
#             if not 0 <= nx < n and not 0 <= ny < n:
#                 if arr[x - dx[m]][y - dy[m]] == 1:
#                     return print(cnt)
#                 else:
#                     x, y = x - dx[m], y - dy[m]


n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

# move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
move = [(0, -1), (-1, 0), (0, 1), (1, 0)]
cnt = 0

while True:
    # 청소 가능한지 check
    if not arr[r][c]:
        arr[r][c] = 2
        cnt += 1

    # 후진 시키거나 정지하기
    for x, y in move:
        dx = r + x
        dy = c + y

        if not arr[dx][dy]:
            break
    else:
        x, y = move[(d - 1) % 4]
        dx = r + x
        dy = c + y
        if arr[dx][dy] == 1:
            break
        else:
            r = dx
            c = dy
            continue

    # 전진하고 기준 방향에 따라서 회전 시키기
    x, y = move[d]
    dx = r + x
    dy = c + y
    d = (d - 1) % 4

    if not arr[dx][dy]:
        r = dx
        c = dy
        continue

print(cnt)
