from itertools import permutations

def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    
    for p in permutations(dungeons, n):
        cnt = 0
        hp = k
        for temp in p:
            if hp >= temp[0]:
                hp -= temp[1]
                cnt += 1
                
        answer = max(cnt, answer)
            
    return answer