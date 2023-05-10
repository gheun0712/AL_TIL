def DFS(x, y, k):
    global res1, res0, res_1
    check = paper[x][y]
    for i in range(x, x + k):
        for j in range(y, y + k):
            if paper[i][j] != check:
                for a in range(3):
                    for b in range(3):
                        DFS(x + a * k // 3, y + b * k // 3, k // 3)
                return

    if check == -1:
        res_1 += 1
    elif check == 0:
        res0 += 1
    elif check == 1:
        res1 += 1


n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

res1 = 0
res0 = 0
res_1 = 0

DFS(0, 0, n)
print(res_1)
print(res0)
print(res1)
