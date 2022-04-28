# 15650_N과M(2)
# 2022-04-28

from itertools import combinations

n, m = map(int, input().split())

res = combinations(range(1, n+1), m)
for i in res:
    print(*i)
