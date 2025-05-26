board = [[0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]]

# board = [[0, 0, 0, 0, 0], 
#          [0, 0, 0, 0, 0], 
#          [0, 0, 0, 0, 0], 
#          [0, 0, 1, 1, 0], 
#          [0, 0, 0, 0, 0]]
dot = []
boom_num = 0
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == 1:
            dot.append([i,j])
            boom_num += 1


for i in range(0,boom_num):
    a = dot[i][i]
    b = dot[i][i+1]
    if a != 0:
        board[a-1][b] = 1
        if b != 0:
            board[a-1][b-1] = 1
        if b != len(board):
            board[a-1][b+1] = 1
    if b != 0:
        board[a][b-1] = 1
    if b != len(board):
        board[a][b+1] = 1
    if b != len(board):
        if b != 0:
            board[a+1][b-1] = 1
        board[a+1][b] = 1
        if b != len(board):
            board[a+1][b+1] = 1
# # 위아래 (십자)
# board[i-1][j-1] | board[i-1][j]    | board[i-1][j+1]
# ====================================================
# board[i][j-1]   | board[i][j]      | board[i][j+1]

# board[i+1][j-1] | board[i+1][j+1]  | board[i+1][j+1]
# [[0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 0], 
#  [0, 1, 1, 1, 0], 
#  [0, 1, 1, 1, 0]]



answer = 0
for h in range(len(board)):
    for k in range(len(board)):
        if board[h][k] == 0:
            answer += 1

print(answer)
print(boom_num)





