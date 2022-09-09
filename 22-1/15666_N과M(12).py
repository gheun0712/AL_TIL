# 15666_N과M(12)
# 2022-05-11

from itertools import combinations_with_replacement

n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
lst = list(combinations_with_replacement(lst, m))

lst = sorted(list(set(lst)))

for i in lst:
    print(*i)
