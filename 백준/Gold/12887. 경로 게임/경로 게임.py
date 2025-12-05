from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = 2,int(input())
d = [input(),input()]
r = d[0].count(".") + d[1].count(".")

ans = int(1e9)
for k in range(2):
    if d[k][0] == "#":
        continue
    queue = deque([(k,0)])
    visited = [[0]*m,[0]*m]
    while queue:
        x,y = queue.popleft()
        if y == m-1:
            ans = min(ans,visited[x][y])
            break
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and d[nx][ny] == ".":
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
print(r-ans-1)