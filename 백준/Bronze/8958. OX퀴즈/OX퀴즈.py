N = int(input())

for _ in range(N):
    cnt = 0
    temp = 1
    lst = list(input())
    for i in lst:
        if i == 'O':
            cnt += temp
            temp += 1
        else:
            temp = 1
    print(cnt)