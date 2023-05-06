def solution(my_string, n):
    answer = ''
    for string in my_string:
        for _ in range(n):
            answer += string
    return answer