# 2022-10-15
# 1157_단어공부

s = input().upper()
s2 = list(set(s))
lst = list()

for i in s2:
    lst.append(s.count(i))

if lst.count(max(lst)) > 1:
    print('?')

else:
    print(s2[lst.index(max(lst))])
