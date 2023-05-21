def solution(n, s):
    if n > s:
        return [-1]
    
    # 원소가 같거나 차이가 최소일때 곱이 최대임
    div = s // n
    temp = s % n
    ans = [div] * n
    
    for i in range(temp):
        ans[i] += 1
    
    ans.sort()
    
    return ans