import sys

n = int(sys.stdin.readline())
lst = []
cnt = 0

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

check = [[0] * n for _ in range(n)]
# 시작점
check[0][0] = 1

for i in range(n):
    for j in range(n):
        # 마지막 칸 도달시, 답 출력
        if i == j == n-1:
            print(check[i][j])
            break

        # 오른쪽 탐색
        if j + lst[i][j] < n:
            check[i][j + lst[i][j]] += check[i][j]

        # 아래 탐색
        if i + lst[i][j] < n:
            check[i+lst[i][j]][j] += check[i][j]
