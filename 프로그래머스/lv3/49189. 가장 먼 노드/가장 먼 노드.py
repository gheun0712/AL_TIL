from collections import deque

def solution(n, edge):
    g = [[] for _ in range(n+1)]
    check = [0] * (n+1)
    
    for i, j in edge:
        g[i].append(j)
        g[j].append(i)
    
    q = deque([1])
    check[1] = 1
    
    while q:
        x = q.popleft()
        
        for n in g[x]:
            if not check[n]:
                check[n] = check[x] + 1
                q.append(n)
        
    answer = check.count(max(check))
            
    return answer