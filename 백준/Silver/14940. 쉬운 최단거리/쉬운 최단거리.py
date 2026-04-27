from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

m,n= map(int,input().split())
map = [list(map(int,input().split())) for _ in range(m)]

for i in range(m):
    for j in range(n):
        if map[i][j] == 2:
            x,y = i,j

queue = deque([(x,y)])
distance = [[-1]*n for _ in range(m)]
distance[x][y] = 0
for i in range(m):
    for j in range(n):
        if map[i][j] == 0:
            distance[i][j] = 0
visited = [[False]*n for _ in range(m)]
visited[x][y] = True
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and map[nx][ny]:
            visited[nx][ny] = True
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx,ny))
for i in distance:
    print(*i)