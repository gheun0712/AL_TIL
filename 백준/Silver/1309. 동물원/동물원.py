import sys

input = sys.stdin.readline

n = int(input())
dp = [[0, 0, 0] for _ in range(n)]
dp[0] = [1, 1, 1]  # 좌, 우, 안채우기

for i in range(1, n):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901

print(sum(dp[n - 1]) % 9901)