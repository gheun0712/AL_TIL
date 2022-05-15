# 2293_동전1
# 2022-05-12



n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [1] + [0]*k
for i in coin:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[-1])