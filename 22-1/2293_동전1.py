# 2293_동전1
# 2022-05-12

"""
동전 가치별 조합 만들어서  k원이 되도록 해야함
도든 경우의 수에 대해서 체킹해야함
점화식으로 찾아보자!
표를 만들어서 각 코인별 상황 체킹해보기

dp[n] = dp[n] + dp[n-k]
이전 n원을 만들 수 있는 경우의 수 + 현재 동전 가치에서 k원을 뺀 가치

Pypy3 => 136ms
Python 3 => 300ms
"""

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [1] + [0]*k
for i in coin:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[-1])