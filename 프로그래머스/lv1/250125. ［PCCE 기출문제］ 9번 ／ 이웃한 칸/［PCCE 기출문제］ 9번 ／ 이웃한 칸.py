def solution(board, x, y):
    n = len(board)
    cnt = 0
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)
    for i in range(4):
        nx,ny = dx[i]+x,dy[i]+y
        if 0<=nx<n and 0<=ny<n:
            if board[x][y] == board[nx][ny]:
                cnt += 1
    return cnt