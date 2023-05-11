import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = []
    ans = 0

    for _ in range(2):
        lst.append(list(map(int, input().split())))

    # 위/아래 불가 대각선으로 지그재그 탐색
    if n > 1:
        lst[0][1] += lst[1][0]
        lst[1][1] += lst[0][0]

    for i in range(2, n):
        lst[0][i] += max(lst[1][i - 1], lst[1][i - 2])
        lst[1][i] += max(lst[0][i - 1], lst[0][i - 2])

    print(max(lst[0][n - 1], lst[1][n - 1]))
