from collections import deque

def solution(board):
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, -1, 1]
    depth = len(board)
    visited = [[0] * depth for _ in range(depth)]
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        
        while q:
            a, b = q.popleft()
            # visited[a][b] = 1
            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b
                
                if 0 <= nx < depth and 0 <= ny < depth and visited[nx][ny] != 1:
                    if board[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] += 1
                    else:
                        board[nx][ny] = 2
    
    for i in range(depth):
        for j in range(depth):
            if board[i][j] == 1:
                bfs(i,j)
    
    res = 0
    for i in range(depth):
        res += board[i].count(0)
    return res