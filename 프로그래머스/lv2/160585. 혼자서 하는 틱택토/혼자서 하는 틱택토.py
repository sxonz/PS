def solution(board):
    ocn,xcn = 0,0
    
    for i in range(3):
        for j in range(3):
            if board[i][j]=='O':
                ocn += 1
            elif board[i][j]=='X':
                xcn += 1
    if ocn < xcn or ocn - xcn >= 2:
        return 0
    if ocn <= 2:
        return 1
    if xcn + 1 == ocn:
        for i in board:
            if i == 'XXX':
                return 0
        if board[0][0] + board[1][1] + board[2][2] == 'XXX' or board[0][2] + board[1][1] + board[2][0] == 'XXX':
            return 0
        else:
            for i in range(3):
                if board[0][i] + board[1][i] + board[2][i] == 'XXX':
                    return 0
            return 1
    if ocn == xcn:
        for i in board:
            if i == 'OOO':
                return 0
        if board[0][0] + board[1][1] + board[2][2] == 'OOO' or board[0][2] + board[1][1] + board[2][0] == 'OOO':
            return 0
        else:
            for i in range(3):
                if board[0][i] + board[1][i] + board[2][i] == 'OOO':
                    return 0
            return 1