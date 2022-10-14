# 2022-10-14
# 4101_크냐?

while True:
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        break

    if n > m:
        print("Yes")

    else:
        print("No")
