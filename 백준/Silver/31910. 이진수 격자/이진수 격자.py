from collections import deque

dx = (0,1)
dy = (1,0)

n = int(input())
board = [input().split() for _ in range(n)]

queue = deque([(0,0)])

M = [['']*n for _ in range(n)]
M[0][0] += board[0][0]
visited = [[False]*n for _ in range(n)]

tmp = []
while queue:
    x,y = queue.popleft()
    f = [0,0]
    for i in range(2):
        nx,ny = x+dx[i],y+dy[i]
        if nx<n and ny<n:
            if board[nx][ny] == 1:
                f[i] = 1
    cur = M[x][y]
    if f == [0,0]:
        if x+1 < n:
            if not visited[x+1][y]:
                visited[x+1][y] = True
                M[x+1][y] = cur + board[x+1][y]
                queue.append((x+1,y))
            else:
                if cur+board[x+1][y] > M[x+1][y]:
                    M[x+1][y] = cur+board[x+1][y]
        if y+1 < n:
            if not visited[x][y+1]:
                visited[x][y+1] = True
                M[x][y+1] = cur + board[x][y+1]
                queue.append((x,y+1))
            else:
                if cur+board[x][y+1] > M[x][y+1]:
                    M[x][y+1] = cur+board[x][y+1]
    if f[0] == 1:
        if not visited[x][y+1]:
            visited[x][y+1] = True
            M[x][y+1] = cur + board[x][y+1]
            queue.append((x,y+1))
        else:
            if cur+board[x][y+1] > M[x][y+1]:
                M[x][y+1] = cur+board[x][y+1]
    if f[1] == 1:
        if not visited[x+1][y]:
            visited[x+1][y] = True
            M[x+1][y] = cur + board[x+1][y]
            queue.append((x+1,y))
        else:
            if cur+board[x+1][y] > M[x+1][y]:
                M[x+1][y] = cur+board[x+1][y]
print(int(M[n-1][n-1],2))