from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    q.append([begin, 0])

    while q:
        x, cnt = q.popleft()
        
        if x == target:
            return cnt
        
        for i in range(0, len(words)):
            temp = 0
            word = words[i]
            
            for j in range(len(x)):
                if x[j] != word[j]:
                    temp += 1
                    
            # 한개의 알파벳만 바꿨을 경우
            if temp == 1:
                q.append([word, cnt + 1])
                
    return 0
    
