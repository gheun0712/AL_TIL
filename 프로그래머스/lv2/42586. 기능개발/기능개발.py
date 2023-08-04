def solution(progresses, speeds):
    answer = []
    cnt = 0
    finish = 0
    
    while progresses:
        if progresses[0] + cnt * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            finish += 1
        else:
            if finish > 0:
                answer.append(finish)
                finish = 0
            else:
                cnt += 1
                
    answer.append(finish)
    return answer