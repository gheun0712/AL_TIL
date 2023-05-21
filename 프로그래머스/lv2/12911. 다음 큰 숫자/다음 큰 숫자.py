def solution(n):
    temp = n + 1
    while True:
        if bin(temp).count('1') == bin(n).count('1'):
            return temp
        temp += 1