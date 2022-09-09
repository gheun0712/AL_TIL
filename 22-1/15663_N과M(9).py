# 15663_N과M(9)
# 2022-05-11

from itertools import permutations

n, m = map(int, input().split())
lst = (map(int, input().split()))
lst = list(permutations(lst, m))
lst = sorted(list(set(lst)))

for i in lst:
    print(*i)
