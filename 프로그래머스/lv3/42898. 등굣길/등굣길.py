def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    # 집 위치
    dp[1][1] = 1
    
    # 웅덩이 위치
    for i, j in puddles:
        dp[j][i] = -1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 웅덩이인 경우에는 패스
            # 대신 경로 더해줘야 하기 때문에 0으로 바꿔주기
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            # 위랑 왼쪽에서 내려옴
            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % 1000000007 
    
    return(dp[n][m]) 