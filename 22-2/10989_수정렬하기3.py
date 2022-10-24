# 2022-10-23
# 10989_수 정렬하기3

import sys

N = int(sys.stdin.readline())
num_lst = [0] * 10001

for _ in range(N):
    temp = int(sys.stdin.readline())
    num_lst[temp] += 1

for i in range(10001):
    if num_lst[i] != 0:
        for j in range(num_lst[i]):
            print(i)


