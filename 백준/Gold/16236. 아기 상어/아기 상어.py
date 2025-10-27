from collections import deque

dx = (-1,0,1,0)
dy = (0,-1,0,1)

n = int(input())
d = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        if d[i][j] == 9:
            d[i][j] = 0
            x,y = i,j

eaten =[[0]*n for i in range(n)]
eaten[x][y] = 1

ate = 0
size = 2

def bfs():
    global x,y,size,ate
    queue = deque([(x,y,0)])
    visited = [[False]*n for i in range(n)]
    visited[x][y] = True
    can = []
    while queue:
        cx,cy,dis = queue.popleft()
        if 0 < d[cx][cy] < size and not eaten[cx][cy]:
            can.append((cx,cy,dis))
            continue

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i] 
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and d[nx][ny] <= size:
                    visited[nx][ny] = True
                    queue.append((nx,ny,dis+1))
    if not can:
        return 0
    rx,ry,dis = min(can,key=lambda x:(x[2],x[0],x[1]))
    ate += 1
    if ate == size:
        size += 1
        ate = 0
    x,y = rx,ry
    eaten[x][y] = True
    return dis

t = 0
while True:
    r = bfs()
    if r:
        t += r
    else:
        break
print(t)