from itertools import permutations

def solution(numbers):
    lst = list(map(str,numbers))
    ans = sorted(lst, key=lambda x: x * 3, reverse = 1)
    return str(int("".join(ans)))