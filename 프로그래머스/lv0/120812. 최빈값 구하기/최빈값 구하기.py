def solution(arr):
    check = [0] * (max(arr)+1) 
    
    for i in arr:
        check[i] += 1
    
    m = 0 #최빈값 갯수 체크
    for c in check:
        if c == max(check):
            m += 1
    
    if m > 1:
        return -1
    else:
        return check.index(max(check))