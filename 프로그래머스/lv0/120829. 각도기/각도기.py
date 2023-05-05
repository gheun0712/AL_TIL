def solution(angle):
    if 0 < angle < 90:
        ans = 1
    elif angle == 90:
        ans = 2
    elif 90 < angle <180:
        ans = 3
    else:
        ans = 4
        
    return ans