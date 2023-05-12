from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    lst = input()[1:-1].split(',')

    q = deque(lst)
    # 뒤집는 경우는 홀수일 때만 한 번 뒤집어 주면 되니깐 R 갯수 확인용 변수
    flag = 0

    # 비어있는 배열
    if n == 0:
        q = []

    for i in p:
        if i == 'R':
            flag += 1

        elif i == 'D':
            if len(q) == 0:
                print("error")
                break
            # 짝수일 경우 뒤집기 없기 때문에 제일 왼쪽 원소 버리기
            # 홀수일 경우 뒤집기 때문에 제일 오른쪽 원소 버리기
            else:
                if flag % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    else:
        if flag % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")