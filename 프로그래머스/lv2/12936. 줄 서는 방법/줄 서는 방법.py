import math

def solution(n, k):
    lst = [i for i in range(1, n+1)]
    answer = []
    
    while lst:
        a = (k-1) // math.factorial(n-1)
        answer.append(lst.pop(a))
        k = k % math.factorial(n-1)
        n -= 1
    
    return answer