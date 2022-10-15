# 2022-10-15
# 2562_최댓값

lst = []

for _ in range(9):
    lst.append(int(input()))

print(max(lst))
print(lst.index(max(lst))+1)
