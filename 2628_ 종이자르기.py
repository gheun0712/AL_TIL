# 2628_종이자르기
# 2022-02-18


def my_diff(arr):
    max_diff = 0
    for i in range(len(arr) - 1):
        now_diff = arr[i + 1] - arr[i]
        if now_diff > max_diff:
            max_diff = now_diff
    return max_diff


col, row = map(int, input().split())  # 가로 세로 길이 받기
N = int(input())  # 잘라야하는 점선의 개수
col_lst = [0, col]
row_lst = [0, row]

for _ in range(N):
    dir, cut_num = map(int, input().split())  # 잘라야하는 방향, 자르는 번호

    if dir == 0:
        row_lst.append(cut_num)
    else:
        col_lst.append(cut_num)

col_lst.sort()
row_lst.sort()

max_row = my_diff(col_lst)
max_col = my_diff(row_lst)

print(max_row * max_col)
