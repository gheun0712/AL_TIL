def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        ans = common[1] - common[0] + common[len(common)-1]
    else:
        ans = common[1] // common[0] * common[len(common)-1]
    return ans
