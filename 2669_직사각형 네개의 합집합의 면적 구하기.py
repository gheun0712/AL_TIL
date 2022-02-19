
# 2669_직사각형 네개의 합집합의 면적 구하기 문제풀이

import sys

sys.stdin = open('input.txt', 'r')

lst = [[0 for _ in range(101)] for _ in range(101)]
ans = 0

for _ in range(1, 5):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if lst[j][i] == 0:
                lst[j][i] = 1
                ans += 1
print(ans)
