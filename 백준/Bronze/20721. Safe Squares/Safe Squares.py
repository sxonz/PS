from collections import deque
dx,dy=(1,-1,0,0),(0,0,1,-1)
n=8
d = [list(input()) for _ in range(n)]
board = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if d[i][j] == 'R':
            for k in range(n):
                board[i][k] = True
            for l in range(n):
                board[l][j] = True
res=0
for i in board:
    res += i.count(False)
print(res)
