from itertools import product

def solution(word):
    answer = []
    lst = ["A", "E", "I", "O", "U"]
    
    for i in range(1, 6):
        for w in product(lst, repeat=i):
            answer.append(''.join(list(w)))
    
    answer.sort()
    
    return answer.index(word) + 1