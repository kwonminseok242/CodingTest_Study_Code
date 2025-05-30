def solution(keyinput, board):

    a = board[0]//2
    b = board[1]//2
    x1 = 0
    x2 = 0
    for i in keyinput:

        if 'left' == i and x1 > -a:
            x1 -= 1 
        if 'right'== i and x1 < a:
            x1 += 1
        if "up" == i and x2 < b:
            x2 += 1
        if 'down' ==i and x2 > -b:
            x2 -= 1
    
    return [x1,x2]

