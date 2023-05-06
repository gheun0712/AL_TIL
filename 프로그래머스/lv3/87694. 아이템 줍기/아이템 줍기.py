from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    field = [[5] * 102 for _ in range(102)]  # 5는 맨처음 땅
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 사각형 범위 내부일때
                if x1 < i < x2 and y1 < j < y2:  
                    field[i][j] = 0
                # 테두리일때
                elif field[i][j] != 0:  
                    field[i][j] = 1 

    # 길 찾기 (최단거리는 BFS)
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[0] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        
        # 아이템 위치에 도착했을때
        if x == itemX * 2 and y == itemY * 2:
            answer = (visited[x][y] - 1) // 2
            break
            
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if visited[nx][ny] == 0 and field[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return answer