# 11660_구간_합_구하기5
# 2022-05-17

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
square = [list(map(int,input().split())) for _ in range(n)]
for k in range(2):
    for i in range(n):
        if k == 1 and i == 0:
            continue
        for j in range(n):
            if k == 0:
                if j == 0:
                    continue
                square[i][j] += square[i][j-1]
            else:
                square[i][j] += square[i-1][j]


for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        print(square[x2-1][y2-1])
    elif x1 == 1:
        print(square[x2-1][y2-1] - square[x2-1][y1-2])
    elif y1 == 1:
        print(square[x2-1][y2-1] - square[x1-2][y2-1])
    else:
        print(square[x2-1][y2-1] - square[x1-2][y2-1] - square[x2-1][y1-2] + square[x1-2][y1-2])
