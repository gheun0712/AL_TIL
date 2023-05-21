def solution(s):    
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        # i == ')'인 경우
        else:
            # 첫 시작인 경우 // 스택이 비어있는 경우
            if stack == []:
                return False
            # 이미 stack에 있는 경우 앞에 저장된 stack 빼기 (쌍으로 맞춰줘야하기 때문)
            else:
                stack.pop()
                
    # 짝 다 찾아서 비어있으면 true // 아직 남아있으면 false
    return stack == []