# 14499_주사위_굴리기
# 22-03-26


# 주사위의 움직임이 칸의 범위 내에 있는지를 체크
def check(k):
    global print_check
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < n and 0 <= ny < m:
        print_check = 1
        return True
    else:
        return False


# 이동칸의 숫자가 0일때와 0이 아닐때의 값 변화
def copy(k):
    if arr[x + dx[k]][y + dy[k]] == 0:
        arr[x + dx[k]][y + dy[k]] = dice[0]
    else:
        dice[0] = arr[x + dx[k]][y + dy[k]]
        arr[x + dx[k]][y + dy[k]] = 0


n, m, x, y, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
move = list(map(int, input().split()))
# 문제 그림 기준으로 dice[0] ~ dice[5] 까지 1,5,6,2,4,3 순서
dice = [0, 0, 0, 0, 0, 0]
# 시작위치 설정
dice[0] = arr[x][y]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
print_check = 0

for i in range(k):
    # 각 움직임 체크
    if move[i] == 1:
        if check(move[i]):
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
            copy(move[i])

    elif move[i] == 2:
        if check(move[i]):
            dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
            copy(move[i])

    elif move[i] == 3:
        if check(move[i]):
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
            copy(move[i])

    elif move[i] == 4:
        if check(move[i]):
            dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
            copy(move[i])

    if print_check:
        print(dice[2])
        x = x + dx[move[i]]
        y = y + dy[move[i]]
        print_check = 0
