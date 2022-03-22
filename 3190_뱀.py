# 3190_뱀
# 2022-03-22

def change(d, c):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


def move():
    # 뱀 첫 위치
    x, y = 1, 1
    # 뱀이 있는 위치는 2로 표시해줌
    map_lst[x][y] = 2
    # 처음엔 우측이동
    d = 0
    time = 0
    # 다음 방향 나타낼 변수
    next = 0
    q = [(x, y)]

    while True:
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 1 <= nx < n and 1 <= ny < n and map_lst[nx][ny] != 2:
                # 사과가 없으면 꼬리 없애기
                if map_lst[nx][ny] == 0:
                    map_lst[nx][ny] = 2
                    q.append((nx, ny))
                    nnx, nny = q.pop(0)
                    map_lst[nnx][nny] = 0

                # 사과가 있으면 꼬리 남겨두기
                if map_lst[nx][ny] == 1:
                    map_lst[nx][ny] = 2
                    q.append((nx,ny))

            else:
                time += 1
                break

            # 다음 위치로 머리를 이동시켜줌
            x, y = nx, ny
            time += 1

            if next < 1 and time == direction[next][0]:
                d = change(d, map_lst[next][1])
                next += 1
        return time


n = int(input())
k = int(input())
map_lst = [[0] * (n+1) for _ in range(n+1)]
direction = []

for _ in range(k):
    x, y = map(int, input().split())
    map_lst[x][y] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    direction.append((int(x), c))

print(move())


