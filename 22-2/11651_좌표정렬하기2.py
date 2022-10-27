# 11651_좌표정렬하기2
# 2022-10-27

N = int(input())
num_lst = []

for _ in range(N):
    x, y = map(int, input().split())
    num_lst.append((x, y))

num_lst.sort(key=lambda x: (x[1], x[0]))

for i in num_lst:
    print(i[0], i[1])
