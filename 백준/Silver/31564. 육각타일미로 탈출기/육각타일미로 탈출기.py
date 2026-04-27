import sys
from collections import deque
dx = (-1,-1,0,1,1,0)
dy = (0,1,1,1,0,-1)
dy2 = (-1,0,1,0,-1,-1)
input = sys.stdin.readline
n,m,k = map(int,input().split())
board = [[True]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
visited[0][0] = True
for _ in range(k):
    a,b = map(int,input().split())
    board[a][b] = False
cnt = n*m - k
ans = -1

queue = deque([(0,0,0)])
while queue:
    temp = queue.popleft()
    x,y,depth = temp[0],temp[1],temp[2]
    if x == n-1 and y == m-1:
        print(depth)
        break
    for i in range(6):
        nx = x+dx[i]
        if x % 2 != 0:
            ny = y+dy[i]
        else:
            ny = y+dy2[i]
        if 0<=nx<n and 0<=ny<m:
            if not(visited[nx][ny]) and board[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx,ny,depth+1])
else:
    print(-1)