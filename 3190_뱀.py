# 3190_뱀
# 2022-03-22


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulate():
    # 뱀의 머리 위치
    x, y = 1, 1
    # 뱀 있는 위치 2로 표시
    data[x][y] = 2
    # 처음은 우측 이동
    direction = 0
    time = 0
    # 다음 회전
    next_direction = 0
    q = [(x, y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            # 사과 없으면 꼬리 빼기
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 꼬리는 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))

        # 벽이나 뱀의 몸통과 부딪히는 경우에는 패스패스
        else:
            time += 1
            break

        # 다음 위치로 머리를 이동
        x, y = nx, ny
        time += 1
        # 다음 회전으로
        if next_direction < l and time == info_direction[next_direction][0]:
            direction = turn(direction, info_direction[next_direction][1])
            next_direction += 1
    return time


n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info_direction = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info_direction.append((int(x), c))

print(simulate())
