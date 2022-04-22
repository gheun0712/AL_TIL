# 11047_동전0
# 2022-04-22

n, k = map(int, input().split())
coin = sorted([int(input()) for _ in range(n)], reverse=True)
cnt = 0

for i in range(n):
    cnt += k // coin[i]
    k %= coin[i]

print(cnt)