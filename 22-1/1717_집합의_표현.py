# 1717_집합의_표현
# 2022-05-18

"""
sys.setrecursionlimit(10**6) 요거 사용하기!
union-find 자료구조 문제!
루트노드가 작은 수를 공통으로 갖도록 합치는 연산
첫번째 인자가 0이면 union_find를 수행하도록 하기
1이면 find_parent로 비교하도록 하기

PyPy3 => 356ms
Python3 => 360ms
"""
import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def find_parent(parent, k):
    if k != parent[k]:
        parent[k] = find_parent(parent, parent[k])
    return parent[k]


def union_find(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    z, a, b = map(int, input().split())
    if z == 0:
        union_find(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
