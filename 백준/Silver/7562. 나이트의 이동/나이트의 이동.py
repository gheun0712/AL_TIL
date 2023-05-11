from collections import deque


def BFS(x1, y1, x2, y2):
    q = deque()
    q.append([x1, y1])
    visited[x1][y1] = 1

    # 나이트 이동 가능한 범위
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    while q:
        x, y = q.popleft()

        # 목표에 도달하면 값 반환
        if x == x2 and y == y2:
            return visited[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1


t = int(input())

for _ in range(t):
    n = int(input())
    curr_x, curr_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    visited = [[False] * n for _ in range(n)]

    if curr_x == goal_x and curr_y == goal_y:
        print(0)
        continue

    ans = BFS(curr_x, curr_y, goal_x, goal_y)
    print(ans)
