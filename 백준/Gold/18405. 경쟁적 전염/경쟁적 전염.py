from collections import deque

n,k = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
s,qx,qy = map(int,input().split())
queue = []
visited = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if d[i][j]:
            queue.append((0,d[i][j],i,j))
            visited[i][j] = d[i][j]
queue.sort()
queue = deque(queue)

dx = (-1,1,0,0)
dy = (0,0,-1,1)

while queue:
    sec,c,x,y = queue.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                if sec < s:
                    visited[nx][ny] = visited[x][y]
                    queue.append((sec+1,visited[nx][ny],nx,ny))
print(visited[qx-1][qy-1])
