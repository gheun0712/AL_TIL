# 15652_N과M(4)
# 2022-04-28


from itertools import combinations_with_replacement

n, m = map(int, input().split())
li = []
for i in range(1, n + 1):
    li.append(i)

for each in list(combinations_with_replacement(li, m)):
    for num in each:
        print(num, end=" ")
    print()
