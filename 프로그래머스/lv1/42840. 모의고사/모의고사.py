def solution(answers):
    ans = [0, 0, 0]
    res = []
    A = [1, 2, 3, 4, 5] # 5개
    B = [2, 1, 2, 3, 2, 4, 2, 5] # 8개
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10개
    
    for idx, answer in enumerate(answers):
        if answer == A[idx % len(A)]:
            ans[0] += 1
        if answer == B[idx % len(B)]:
            ans[1] += 1
        if answer == C[idx % len(C)]:
            ans[2] += 1
    
    
    for idx, score in enumerate(ans):
        if score == max(ans):
            res.append(idx+1)
            
    return res