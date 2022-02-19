# 1244_스위치_켜고_끄기

T = int(input())  # 스위치 개수
switch_lst = list(map(int, input().split()))
switch_lst.insert(0, 3)
stu_num = int(input())  # 학생 수

for stu in range(stu_num):
    # gen : 성별, n : 받은 스위치 수
    gen, n = map(int, input().split())

    if gen == 1:
        for i in range(n, T + 1, n):
            switch_lst[i] = 1 if switch_lst[i] == 0 else 0
    else:
        # 스위치 범위 벗어났을 때 처리하는 방법
        # 본인 스위치만 반대로 켰다 껐다 해줌
        if n > T and n < 1:
            switch_lst[n] = 1 if switch_lst[n] == 0 else 0
        else:
            i = 0
            while 1 <= (n + i) <= T and 1 <= (n - i) <= T:  # n: 배정받은 스위치 번호  T: 스위치 개수
                if switch_lst[n + i] == switch_lst[n - i]:
                    # if i == 0:
                    #     switch_lst[n + i] = 1 if switch_lst[n + i] == 0 else 0
                    # else:
                    switch_lst[n + i] = 1 if switch_lst[n + i] == 0 else 0
                    switch_lst[n - i] = 1 if switch_lst[n + i] == 1 else 0
                    i += 1
                else:
                    break

p = 1
while 1:
    print(*switch_lst[p:(p+20)], sep=' ')
    if T < 20:
        break
    T -= 20
    p += 20
# print(*switch_lst[1:21])










