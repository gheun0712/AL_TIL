from collections import Counter

def solution(topping):
    answer = 0
    n = len(topping)
    x = Counter(topping)
    y = set()
    
    for t in topping:
        x[t] -= 1
        if x[t] == 0:
            del x[t]
        y.add(t)
        
        if len(x.keys()) == len(y):
            answer += 1

    return answer