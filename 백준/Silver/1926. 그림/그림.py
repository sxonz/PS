from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs():
    s = 1
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and d[nx][ny] == '1':
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    s += 1          
    return s

n,m = map(int,input().split())
d = [input().split() for _ in range(n)]

queue = deque([])
visited = [[False]*m for _ in range(n)]

cnt = 0
size = []
for i in range(n):
    for j in range(m):
        if not visited[i][j] and d[i][j] == '1':
            visited[i][j] = True
            queue.append((i,j))
            size.append(bfs())
            cnt += 1

print(cnt)
if cnt == 0:
    print(0)
else:
    print(max(size))