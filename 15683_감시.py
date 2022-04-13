# 15683_감시
# 2022-04-13

"""
감시카메라 방향이 90도로 회전가능함
1번 : 한방향
2번 : 양족방향
3번 : 이웃방향
4번 : 3방향
5번 : 4방향

bfs 탐색 > 벽 일때 == 6 continue / 탐색 가능하면 # > 상관없는 수 9로 바꿔주기
카메라 탐색 기준방향을 90도로 돌려줘야함
카메라가 1개가 아니라 최대 8개인데, 각 카메라 별로 회전해서 경우의 수 구해줘야함
>> 카메라 별로 분류해서 조건 걸어주기
**사각 지대의 최소 크기** >> 최대 크기를  res에 넣어주는데 n*m으로 넣어주면 될듯
"""


def monitor(idx, direction, info):
    if camera[idx][2] == 1:
        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9

            row = row + dx[direction]
            col = col + dy[direction]

    elif camera[idx][2] == 2:
        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9

            row = row + dx[direction]
            col = col + dy[direction]

        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9
            # 서로 반대방향으로 뻗어나가기
            row = row + dx[direction+2]
            col = col + dy[direction+2]

    elif camera[idx][2] == 3:
        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9
            # 바로 옆 이웃하는 방향으로 뻗어나가기
            row = row + dx[direction-1]
            col = col + dy[direction-1]

        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9

            row = row + dx[direction]
            col = col + dy[direction]

    elif camera[idx][2] == 4:
        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9
            # 3방향으로 이웃해서 뻗어나가기
            row = row + dx[direction-2]
            col = col + dy[direction-2]

        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9

            row = row + dx[direction-1]
            col = col + dy[direction-1]

        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9

            row = row + dx[direction]
            col = col + dy[direction]

    elif camera[idx][2] == 5:
        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9
            # 4방향으로 뻗어나가기
            row = row + dx[direction]
            col = col + dy[direction]

        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9

            row = row + dx[direction+1]
            col = col + dy[direction+1]

        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9

            row = row + dx[direction+2]
            col = col + dy[direction+2]

        row = camera[idx][0]
        col = camera[idx][1]

        while 0 <= row < n and 0 <= col < m and info[row][col] != 6:
            if info[row][col] == 0:
                info[row][col] = 9

            row = row + dx[direction+3]
            col = col + dy[direction+2]


def find(cnt, lst):
    global res

    if cnt == len(camera):
        temp = 0
        for i in range(n):
            temp += lst[i].count(0)
        res = min(res, temp)
        return

    for i in range(dc[camera[cnt][2]]):
        off = [idx[:] for idx in lst]
        monitor(cnt, i, off)
        find(cnt+1, off)


n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
res = n * m
camera = []

for i in range(n):
    for j in range(m):
        # 카메라는 1-5까지 범위
        if 0 < info[i][j] < 6:
            # 카메라 존재하는 위치 저장 (row, col, 카메라번호)
            camera.append([i, j, info[i][j]])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 인덱스 번호 = 카메라 번호 > 탐색 방향 가능한 횟수
dc = [0, 4, 2, 4, 4, 1]
# print(info)
# print(camera)
find(0, info)
print(res)
