from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(input()) for i in range(n)]

visited = [[[False]*m for i in range(n)] for i in range(2)]
distance = [[[int(1e9)]*m for i in range(n)] for i in range(2)]
visited[0][0][0] = True
distance[0][0][0] = 1

queue = deque([(0,0,0)])
while queue:
    x,y,b = queue.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if b == 0:
                if d[nx][ny] == "0" and not visited[0][nx][ny]:
                    visited[0][nx][ny] = True
                    distance[0][nx][ny] = distance[0][x][y] + 1
                    queue.append((nx,ny,0))
                elif d[nx][ny] == "1" and not visited[1][nx][ny]:
                    visited[1][nx][ny] = True
                    distance[1][nx][ny] = distance[0][x][y] + 1
                    queue.append((nx,ny,1))
            else:
                if d[nx][ny] == "0" and not visited[1][nx][ny]:
                    visited[1][nx][ny] = True
                    distance[1][nx][ny] = distance[1][x][y] + 1
                    queue.append((nx,ny,1))

res = min(distance[0][n-1][m-1],distance[1][n-1][m-1])
res = res if res != int(1e9) else -1
print(res)