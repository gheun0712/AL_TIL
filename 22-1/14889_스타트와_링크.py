# 14889_스타트와_링크
# 2022-04-08

"""
능력치를 2차원 배열로 정리해서 조합해서 최소 차이를 구해야 함
조합을 어떻게 해야할지가 문제임 > 무지성 조합은 좀 힘들거 같은데
백트래킹 알고리즘으로 접근해볼까

"""


def find(v, idx):
    global cnt
    if v == n // 2:
        team1 = 0
        team2 = 0

        for i in range(n-1):
            for j in range(i+1, n):
                if visit[i] != 0 and visit[j] != 0:
                    team1 += s[i][j]
                    team1 += s[j][i]

                elif visit[i] == 0 and visit[j] == 0:
                    team2 += s[i][j]
                    team2 += s[j][i]
        cnt = min(cnt, abs(team2-team1))
        return

    for k in range(idx+1, n):
        if visit[k] == 0:
            visit[k] = 1
            find(v+1, k)
            visit[k] = 0


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visit = [0 for _ in range(n)]
visit[0] = 1
cnt = int(1e9)

find(1, 0)
print(cnt)
