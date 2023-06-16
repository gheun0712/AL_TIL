import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst = sorted(lst, key=lambda x: x[0])
    temp = lst[0][1]
    cnt = 1

    for i in range(1, n):
        if lst[i][1] < temp:
            temp = lst[i][1]
            cnt += 1

    print(cnt)
