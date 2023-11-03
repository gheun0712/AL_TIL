# i번째 뜯으면 i-1/i+1 못 뜯음
# i-2의 값이 최대값이기 때문에 i-2에 i번째 값 더해주기
# 첫번째 스티커 뜯으면 DP[0] = sticker[0] > 2번째와 제일 마지막 스티커 못 뜯음
# 뜯지 않으면 DP[0] = 0

def solution(sticker):
    
    # 스티커 갯수가 한개일 경우, 바로 반환해서 빠르게 종료
    if len(sticker) == 1:
        return sticker[0]
    
    dp1 = [0] * len(sticker)
    dp2 = [0] * len(sticker)
    
    # 첫번째꺼 뜯었을때
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i-2]+sticker[i], dp1[i-1])
    
    # 첫번째꺼 안 뜯었을때
    for i in range(1, len(sticker)):
        dp2[i] = max(dp2[i-2]+sticker[i], dp2[i-1])
    
    return max(dp1[-2], dp2[-1])