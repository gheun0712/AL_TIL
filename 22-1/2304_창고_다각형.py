# 2304_창고다각형
# 2022-02-22

N = int(input())

max_row, max_col = 0, 0
array = [[0, 0] for i in range(1001)]

for _ in range(N):
    L, H = list(map(int, input().split()))
    max_row = max(L, max_row)
    max_col = max(H, max_col)
    array[L] = [L, H]

max_value = 0
max_idx = 0
ans = 0

for i in range(1, max_row + 1):
    if array[i] != 0:
        if array[i][1] == max_col:
            max_idx = i

# 기둥 왼쪽편 탐색
for j in range(1, max_idx):
    max_value = max(max_value, array[j][1])
    ans += max_value

max_value = 0

# 기둥 오른쪽편 탐색 (오른쪽에서 왼쪽으로 역방향 탐색)
for k in range(max_row, max_idx, -1):
    max_value = max(max_value, array[k][1])
    ans += max_value

print(max_col + ans)



