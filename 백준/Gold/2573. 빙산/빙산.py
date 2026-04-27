import sys
input = sys.stdin.readline
from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())

d = [list(map(int,input().split())) for _ in range(n)]

def check():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
    cnt = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            if d[i][j] >= 1 and not visited[i][j]:
                cnt += 1
                queue.append((i,j))
                while queue:
                    x,y = queue.popleft()
                    visited[x][y] = True
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<m:
                            if d[nx][ny] >= 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx,ny))


    return True if cnt == 1 else False


visited = [[False]*m for _ in range(n)]
temp = [i[:] for i in d]

year = 0
while check():
    year += 1
    for i in range(n):
        for j in range(m):
            temp[i][j] = d[i][j]
    
    for x in range(n):
        for y in range(m):
            if d[x][y] >= 1:
                for i in range(4):
                    nx,ny = x+dx[i], y+dy[i]
                    if 0<=nx<n and 0<=ny<m:
                        if d[nx][ny] <= 0 and temp[x][y] > 0:
                            temp[x][y] -= 1
                            

    for i in range(n):
        for j in range(m):
            d[i][j] = temp[i][j]

if sum([sum(i) for i in d]) == 0:
    print(0)
else:
    print(year)