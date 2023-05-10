n = int(input())
stack = []
ans = []
flag = 0
current = 1

for _ in range(n):
    num = int(input())
    # 주어진 수에 도달할때까지 stack 쌓아주기
    while current <= num:
        stack.append(current)
        ans.append("+")
        current += 1
    
    # 스택에 쌓인 수가 num과 일치할때 pop
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    # 스택에 쌓인 수보다 뺴야할 목표 숫자가 작은 경우에는 pop 불가
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in ans:
        print(i)