from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())

d = [list(map(int,input().split())) for i in range(n)]
cnt = 0
for i in d:
    cnt += sum(i)

day = 0
while cnt:
    day += 1
    queue = deque([(0,0)])
    visited = [[False]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if d[i][j] == 1:
                d[i][j] = 2
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if d[nx][ny]:
                    d[nx][ny] -= 1
                    if not d[nx][ny]:
                        visited[nx][ny] = True
                        cnt -= 1
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
print(day)