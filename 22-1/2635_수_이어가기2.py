# 2635_ 수_이어가기

N = int(input())
max_num = 0
max_lst = []

for i in range(N + 1):
    num_lst = [N, i]
    j = 0

    while True:
        third = num_lst[j] - num_lst[j + 1]
        if third <= -1:
            break
        num_lst.append(third)

        # 최댓값 구하기
        if max_num < len(num_lst):
            max_num = len(num_lst)
            max_lst = num_lst
        j += 1

print(max_num)
print(*max_lst)
