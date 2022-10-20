# 2022-10-21
# 2675_문자열반복

T = int(input())

for _ in range(T):
    N, S = input().split()
    N = int(N)
    S = str(S)

    for i in range(len(S)):
        print(N*S[i], end='')
    print()