# 1181_단어정렬
# 2022-10-29

N = int(input())
lst = []

for _ in range(N):
    lst.append(input())

temp_lst = set(lst)
lst = list(temp_lst)
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)