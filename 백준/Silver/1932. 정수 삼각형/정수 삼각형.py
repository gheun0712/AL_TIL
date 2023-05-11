n = int(input())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(lst[i])):
        # 제일 왼쪽 라인
        if j == 0:
            lst[i][j] = lst[i][j] + lst[i - 1][j]
        # 제일 오른쪽 라인
        elif j == len(lst[i]) - 1:
            lst[i][j] = lst[i][j] + lst[i - 1][j - 1]
        # 대각선 좌우 비교해서 최댓값일 경우에 이전값에 현재값 더해서 바꿔주기
        else:
            lst[i][j] = max(lst[i - 1][j - 1], lst[i - 1][j]) + lst[i][j]

print(max(lst[n - 1]))
