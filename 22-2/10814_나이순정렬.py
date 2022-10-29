# 10814_나이순정렬
# 2022-10-29

import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    temp = list(map(str, input().split()))
    temp.append(i)
    lst.append(temp)

lst.sort(key=lambda x: (int(x[0]), int(x[2])))

for j in lst:
    print(j[0], j[1])
