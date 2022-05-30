# 16507_어두운건_무서워
# 2022-05-30

"""
(r1, c1) (r2, c2)를 꼭짓점으로 범위 내에 있는 숫자의 평균 구하기
dp 방식으로 탐색 해결
구간 이전을 빼주고 구간 내의 숫자를 더해주기
직접 그림을 그려서 풀어봤습니다!

Pypy3 => 924ms
Python3 => 2008ms
"""

r, c, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

for i in range(1, r + 1):
    for j in range(1, c + 1):
        dp[i][j] = -dp[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] + arr[i - 1][j - 1]

for i in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    ans = dp[r2][c2] - dp[r1 - 1][c2] - dp[r2][c1 - 1] + dp[r1 - 1][c1 - 1]
    total = ((r2 - r1) + 1) * ((c2 - c1) + 1)
    print(ans // total)
