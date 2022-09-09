# 16235_나무_재테크
# 2022-04-22
# 시간초과 실패
"""
한 칸 내에 여러 개의 나무가 심겨져 있을 수 있다.
>> 첫 양분은 한 칸에 5만큼 있음
나이만큼 양분을 먹는다
봄 > 나이만큼 양분먹고 나이+1
나이 어린 나무부터 양분 먹고 양분 부족하면 죽음
여름> 죽은 나무가 양분으로 변하면서  +양분=(나이//2)
가을> 번식해야하는 나이가 5배수 이고 인접한 8칸에 새로운 나무 생성
겨울 > 로봇이 뽈뽈뽈~ 양문의 양은 +A[r][c]
"""
import collections

n, m, k = map(int, input().split())
arr = [[5] * n for _ in range(n)]
robot_oil = []
for _ in range(n):
    robot_oil.append(list(map(int, input().split())))

tree = [[collections.deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

while k > 0:
    k -= 1

    # 봄, 여름
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) != 0:
                temp = 0
                for k in range(len(tree[i][j])):
                    if arr[i][j] >= tree[i][j][k]:
                        arr[i][j] -= tree[i][j][k]
                        tree[i][j][k] += 1

                    else:
                        for m in range(k, len(tree[i][j])):
                            temp += tree[i][j].pop() // 2
                        break

                arr[i][j] += temp

    # 가을, 겨울
    for i in range(n):
        for j in range(n):
            arr[i][j] += robot_oil[i][j]
            for k in tree[i][j]:
                if k % 5 == 0:
                    for m in range(8):
                        nx = i + dx[m]
                        ny = j + dy[m]

                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].appendleft(1)

cnt = 0
for x in range(n):
    for y in range(n):
        cnt += len(tree[x][y])

print(cnt)
