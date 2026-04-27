from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [input() for i in range(n)]
for i in range(n):
    for j in range(m):
        if d[i][j] == 'I':
            queue = deque([(i,j)])
cur = 0
visited = [[False]*m for i in range(n)]
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and d[nx][ny] != 'X':
                visited[nx][ny] = True
                if d[nx][ny] == 'P':
                    cur += 1
                queue.append((nx,ny))
print(cur if cur else 'TT')