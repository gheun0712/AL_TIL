def solution(money):
    # 앞에서부터 터는 경우
    dp = [0] * len(money)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i-1], money[i] + dp[i-2])
    
    # 뒤에서부터 터는 경우
    dp_2 = [0] *len(money)
    dp_2[0] = 0
    dp_2[1] = money[1]
    for i in range(2, len(money)):
        dp_2[i] = max(dp_2[i-1], money[i] + dp_2[i-2])
    
    return max(max(dp), max(dp_2))