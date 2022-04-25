# 17144_미세먼지_안녕
# 2022-04-25

"""
미세먼지 확산 >>
4방향, A(r,c)//5만큼, 남은 양 = 원래양 - 확산양 * 확산방향개수
주의할 점 ! >> 모인 미세먼지 합을 해줘야함, 원래 있는 칸에도 확산 가능

공기청정기 >>
1열에 2칸 차지, 위쪽은 반시께방향, 아래쪽은 시계방향, 바람 방향대로 미세먼지 이동
주의할 점! >> 문제에 주어진 사진처럼 크게 돌아돌아

pypy3 => 476ms
"""

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
time = 0

while time < t:
    temp_arr = [[0] * c for _ in range(r)]

    # 미세먼지 퍼뜨리기
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                cnt = 0

                for k in range(4):
                    nx = i + direction[k][0]
                    ny = j + direction[k][1]

                    if 0 <= nx < r and 0 <= ny < c and a[nx][ny] != -1:
                        temp_arr[nx][ny] += (arr[i][j] // 5)
                        cnt += 1

                arr[i][j] = arr[i][j] - (arr[i][j] // 5) * cnt

    for i in range(r):
        for j in range(c):
            arr[i][j] += temp_arr[i][j]

    temp_arr = [[-2] * c for _ in range(r)]
    machine = 0
    for row in range(r):
        if arr[row][0] == -1:
            machine = row
            break

    # 위쪽 방향
    for i in range(1, c):
        temp_arr[0][i - 1] = arr[0][i]
        temp_arr[machine][i] = arr[machine][i - 1]
        temp_arr[machine][1] = 0

    for i in range(1, machine + 1):
        if arr[i][0] != -1:
            temp_arr[i][0] = arr[i - 1][0]
        temp_arr[i - 1][c - 1] = arr[i][c - 1]

    # 아래쪽 방향
    for i in range(1, c):
        temp_arr[r - 1][i - 1] = arr[r - 1][i]
        temp_arr[machine + 1][i] = arr[machine + 1][i - 1]
        temp_arr[machine + 1][1] = 0

    for i in range(machine + 2, r):
        if arr[i - 1][0] != -1:
            temp_arr[i - 1][0] = arr[i][0]
        temp_arr[i][c - 1] = arr[i - 1][c - 1]

    for i in range(r):
        for j in range(c):
            if temp_arr[i][j] != -2:
                arr[i][j] = temp_arr[i][j]
    time += 1

ans = sum(list(sum(arr, [])))+2
print(ans)
