# 9095_1,2,3더하기
# 2022-04-22

t = int(input())


def sums(num):
    if num == 1:
        return (1)
    elif num == 2:
        return (2)
    elif num == 3:
        return (4)
    else:
        return sums(num - 1) + sums(num - 2) + sums(num - 3)


for i in range(t):
    n = int(input())
    print(sums(n))
