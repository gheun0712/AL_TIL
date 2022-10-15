# 2022-10-15
# 2577_숫자의 개수

a = int(input())
b = int(input())
c = int(input())

ans = a * b * c
lst = list(str(ans))

for i in range(10):
    cnt = lst.count(str(i))
    print(cnt)
