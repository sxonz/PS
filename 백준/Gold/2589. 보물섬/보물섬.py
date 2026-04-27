from collections import deque
dx = (-1,1,0,0)
dy = (0,0,-1,1)
n,m = map(int,input().split())
d = []
result = []
for _ in range(n):
    d.append(input())
for i in range(n):
    for j in range(m):
        if d[i][j] == 'W':
            continue
        visited = [[False]*m for _ in range(n)]
        visited[i][j] = True
        queue = deque([])
        queue.append((i,j,0))
        _max = -1
        while queue:
            x,y,depth = queue.popleft()
            if _max < depth:
                _max = depth
            for t in range(4):
                nx,ny = x+dx[t],y+dy[t]
                if 0<=nx<n and 0<=ny<m:
                    if not visited[nx][ny] and d[nx][ny] == 'L':
                        visited[nx][ny] = True
                        queue.append((nx,ny,depth+1))
        result.append(_max)
print(max(result))