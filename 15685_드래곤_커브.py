# 15685_드래곤_커브
# 2022-04-03

def curve():
    for _ in range(n):
        for x, y, d, g in q:
            visited[x][y] = 1
            direction = [d]

            for _ in range(g):
                for i in range(len(direction) - 1, -1, -1):
                    temp = (direction[i] + 1) % 4
                    direction.append(temp)

            for j in direction:

                x += dx[j]
                y += dy[j]

                if 0 <= x < 101 and 0 <= y < 101:
                    visited[x][y] = 1


n = int(input())
visited = [[0] * 101 for _ in range(101)]
res = 0

# 0, 1, 2, 3 순서대로 이동
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

q = []

for _ in range(n):
    # x, y 방향이 반대이니까 받을때 거꾸로 받아서 입력하면 방향 헷갈리지 않음!
    y, x, d, g = map(int, input().split())
    q.append((x, y, d, g))

curve()

for i in range(100):
    for j in range(100):
        if visited[i][j]:
            # 4부분 다 포함되는지 확인하기!
            if visited[i+1][j] and visited[i][j+1] and visited[i+1][j+1]:
                res += 1

print(res)
