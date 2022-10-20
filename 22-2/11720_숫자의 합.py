# 2022-10-20
# 11720_숫자의 합

N = int(input())
lst = list(input())
sum = 0

for i in range(N):
    sum += int(lst[i])

print("{}".format(sum))
