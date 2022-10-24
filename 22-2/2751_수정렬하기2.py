# 2022-10-24
# 2751_수정렬하기

N = int(input())
num_lst = []

for _ in range(N):
    temp = int(input())
    num_lst.append(temp)

for i in sorted(num_lst):
    print(i)

