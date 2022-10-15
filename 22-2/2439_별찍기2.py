# 2022-10-15
# 2439_별찍기2

N = int(input())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)
