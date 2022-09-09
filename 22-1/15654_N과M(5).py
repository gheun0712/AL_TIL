# 15654_N과M(5)
# 2022-05-10

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
check = [0] * N
res = [0] * M


def dfs(cnt):
    if cnt == M:
        print(*res)
        return

    for i in range(len(num)):
        if check[i] == 1:
            continue

        check[i] = 1
        res[cnt] = num[i]
        dfs(cnt + 1)
        check[i] = 0


dfs(0)
