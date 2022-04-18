# 15686_치킨_배달
# 2022-04-14
# 2022-04-18

"""
최솟값을 구하는 문제 >> 거리의 최솟값이기 때문에 절대값으로 계산하기
M개를 어떻게 골라낼 것인가가 문제
치킨집을 m개만큼 골라내고 최소 치킨거리를 선택하는 순서로 문제풀어보기
0 : 빈칸, 1 : 집, 2: 치킨집
"""


def find(idx, x, y):
    global res

    if idx == m:
        temp = []
        for i in range(n):
            for j in range(n):
                if info[i][j] == 3:
                    temp.append((i, j))

        ans = distance(temp, house)

        if res > sum(ans):
            res = sum(ans)
        return

    else:
        for i in range(x, n):
            if i == x:
                k = y
            else:
                k = 0

            for j in range(k, n):
                if info[i][j] == 2:
                    info[i][j] = 3
                    find(idx+1, i, j+1)
                    info[i][j] = 2


def distance(a, b):
    ans = []
    for i in b:
        temp = int(1e9)
        for j in a:
            diff = abs(i[0]-j[0]) + abs(i[1]-j[1])
            temp = min(temp, diff)
        ans.append(temp)
    return ans


n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
res = int(1e9)
chicken = 0
house = []

for i in range(n):
    for j in range(n):
        if info[i][j] == 1:
            house.append([i, j])
        elif info[i][j] == 2:
            chicken += 1

find(0, 0, 0)
print(res)
