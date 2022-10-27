# 2839_설탕배달
# 2022-10-27

N = int(input())
cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += int(N // 5)
        print(cnt)
        break

    N -= 3
    cnt += 1

else:
    print(-1)
