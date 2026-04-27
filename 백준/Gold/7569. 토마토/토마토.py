from collections import deque

m,n,k = map(int,input().split())
d = [[list(map(int,input().split())) for i in range(n)] for j in range(k)]

dx = (-1,1,0,0,0,0)
dy = (0,0,-1,1,0,0)
dz = (0,0,0,0,-1,1)

cnt = 0
queue = deque([])

for i in range(k):
    for j in range(n):
        for l in range(m):
            if d[i][j][l] == 1:
                queue.append((i,j,l,0))
            elif d[i][j][l] == 0:
                cnt += 1

visited = [[[False]*m for i in range(n)] for j in range(k)]

while queue:
    z,x,y,day = queue.popleft()
    for i in range(6):
        nz,nx,ny = z+dz[i], x+dx[i], y+dy[i]
        if 0<=nz<k and 0<=nx<n and 0<=ny<m:
            if not visited[nz][nx][ny] and d[nz][nx][ny] == 0:
                d[nz][nx][ny] = 1
                visited[nz][nx][ny] = True
                queue.append((nz,nx,ny,day+1))
                cnt -= 1
print(-1 if cnt else day)