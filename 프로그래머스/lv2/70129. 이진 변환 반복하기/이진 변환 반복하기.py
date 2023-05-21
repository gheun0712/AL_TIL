def solution(s):
    answer = []
    
    cnt = 0
    zero = 0
    
    while True:
        if s == "1":
            break
        else:
            zero += s.count("0")
            s = s.replace("0",'')
            temp = len(s)
            s = bin(temp)[2:]
            cnt += 1
            
    answer.append(cnt)
    answer.append(zero)
    
    return answer