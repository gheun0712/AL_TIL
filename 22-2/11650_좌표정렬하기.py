# 2022-10-24
# 11650_좌표정렬하기

N = int(input())
num_lst = []

for _ in range(N):
    x, y = map(int, input().split())
    num_lst.append((x, y))
num_lst.sort()
for i in range(N):
    print(num_lst[i][0],num_lst[i][1])