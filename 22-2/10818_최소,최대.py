# 2022-10-20
# 10818_최소,최대

N = int(input())
lst = list(map(int, input().split()))
min_num = lst[0]
max_num = lst[0]

for num in lst:
    if num > max_num:
        max_num = num

    elif num < min_num:
        min_num = num

print("{} {}".format(min_num, max_num))
