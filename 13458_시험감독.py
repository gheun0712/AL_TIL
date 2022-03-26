# 13458_시험감독
# 2022-03-26

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0

for i in range(N):
    temp = A[i] - B

    if temp < 0:
        temp = 0
    cnt += 1

    cnt += temp // C

    if temp % C != 0:
        cnt += 1

print(cnt)
