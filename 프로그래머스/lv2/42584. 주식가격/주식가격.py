from collections import deque

def solution(prices):
    answer = []
    qeue = deque(prices)
    
    while qeue:
        price = qeue.popleft()
        cnt = 0
        for q in qeue:
            cnt += 1
            if price > q:
                break
        answer.append(cnt)
    
    return answer