from collections import deque

bigx = (-2,2,0,0)
bigy = (0,0,-2,2)
smallx = (-1,1,0,0)
smally = (0,0,-1,1)

cnt = 0
n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == '@':
            x,y = i,j
        elif board[i][j] in ['#','*']:
            cnt += 1

b = 0
queue = deque([])

for i in range(4):
    nx,ny = x+smallx[i],y+smally[i]
    flag = True
    if 0<=nx<n and 0<=ny<m:
        if board[nx][ny] == '|':
            continue
        if board[nx][ny] == '*':
            board[nx][ny] = '.'
            queue.append((nx,ny))
            b += 1
        elif board[nx][ny] == '#':
            board[nx][ny] = '*'
    else:
        flag = False
    if flag:
        nx,ny = x+bigx[i],y+bigy[i]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] == '*':
                board[nx][ny] = '.'
                queue.append((nx,ny))
                b += 1
            elif board[nx][ny] == '#':
                board[nx][ny] = '*'
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx,ny = x+smallx[i],y+smally[i]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] == '*':
                board[nx][ny] = '.'
                queue.append((nx,ny))
                b += 1
            elif board[nx][ny] == '#':
                board[nx][ny] = '*'
print(b,cnt-b)

