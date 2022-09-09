# 9251_LCS
# 2022-05-16

import sys

input = lambda: sys.stdin.readline().strip()

a = input()
b = input()
lst = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            lst[i][j] = lst[i - 1][j - 1] + 1
        else:
            lst[i][j] = max(lst[i][j - 1], lst[i - 1][j])

print(lst[-1][-1])
