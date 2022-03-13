# 2667_단지번호붙이기(DFS)
# 2022-03-13

def DFS(x, y):
    global cnt

    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if g[x][y] == 1:
        # 단지 집 개수 카운팅팅
        cnt += 1
        g[x][y] = 0

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            DFS(x + dx[i], y + dy[i])
        return True


n = int(input())
g = []

for _ in range(n):
    g.append(list(map(int, input())))

chek_lst = []
cnt = 0


for i in range(n):
    for j in range(n):
        if DFS(i, j):
            chek_lst.append(cnt)
            # 다른 단지로 이동하기 위해서 cnt 리셋
            cnt = 0

print(len(chek_lst))
chek_lst.sort()
for k in chek_lst:
    print(k)
