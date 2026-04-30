def solution(board):
    board.insert(0,[2]*(len(board)))
    board.append([2]*(len(board)))
    for i in board:
        i.insert(0,2)
        i.append(2)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                board[i-1][j-1],board[i][j-1],board[i-1][j] = 3,3,3
                if board[i][j+1] != 1:board[i][j+1] = 3
                if board[i+1][j] != 1:board[i+1][j] = 3
                if board[i+1][j-1] != 1:board[i+1][j-1] = 3
                if board[i-1][j+1] != 1:board[i-1][j+1] = 3
                if board[i+1][j+1] != 1:board[i+1][j+1] = 3
    
    print(board)
    cnt = 0
    for i in board:
        cnt += i.count(0)
    return cnt
            