def solution(array):
    array.sort()
    n = (len(array) // 2)
    return array[n]