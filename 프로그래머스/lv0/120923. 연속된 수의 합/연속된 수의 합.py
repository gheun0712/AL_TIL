def solution(num, total):
    aver = total // num
    return [i for i in range(aver - (num-1)//2, aver + (num+2)//2)]