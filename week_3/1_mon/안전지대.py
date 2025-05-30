def solution(board):
    dot = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                dot.append([i, j])

    for d in dot:
        a = d[0]
        b = d[1]

        board[a][b] = 1

        if a > 0 and b > 0:
            board[a-1][b-1] = 1
        if a > 0:
            board[a-1][b] = 1
        if a > 0 and b < len(board)-1:
            board[a-1][b+1] = 1
        if b > 0:
            board[a][b-1] = 1
        if b < len(board)-1:
            board[a][b+1] = 1
        if a < len(board)-1 and b > 0:
            board[a+1][b-1] = 1
        if a < len(board)-1:
            board[a+1][b] = 1
        if a < len(board)-1 and b < len(board)-1:
            board[a+1][b+1] = 1

    
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                answer += 1

    return answer
