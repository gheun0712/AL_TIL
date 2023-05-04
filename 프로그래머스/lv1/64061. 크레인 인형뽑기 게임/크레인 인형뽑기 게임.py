def solution(board, moves):
    bucket = []
    ans = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    ans += bucket[-1:]
                    bucket = bucket[:-2]
                break
    return len(ans)*2