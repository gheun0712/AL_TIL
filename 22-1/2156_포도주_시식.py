# 2156_포도주_시식
# 2022-05-11

"""
가장 많은 양의 와인 합을 구하는 문제
조건에 따라서 합을 구해야 하기 때문에 DP를 통해서 탐색해주자!

DP 배열은 DP[포도주순서][연속으로 마신 횟수] 로 설정해보기

PyPy3 => 156ms
Python3 => 480ms
"""

n = int(input())
wine = []

for _ in range(n):
    wine.append(int(input()))

dp = [[0 for _ in range(3)] for _ in range(n+1)]
dp[0][1] = wine[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + wine[i]
    dp[i][2] = dp[i-1][1] + wine[i]

print(max(dp[n-1]))

