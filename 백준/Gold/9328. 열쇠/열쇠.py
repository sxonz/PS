from collections import deque
dx = (-1,1,0,0)
dy = (0,0,-1,1)
for t in range(int(input())):
    ans = 0
    n,m = map(int,input().split())
    d = [list(input()) for i in range(n)]
    key = input().upper()
    queue = []
    visited = [[0]*m for i in range(n)]
    u = []
    tmp = []
    for i in range(n):
        if d[i][0] in key+'.$' or 97 <= ord(d[i][0]) <= 122:
            queue.append((i,0))
            visited[i][0] = 1
            u.append((i,0))
            if 97 <= ord(d[i][0]) <= 122:
                key += d[i][0].upper()
                d[i][0] = "."
        elif 65 <= ord(d[i][0]) <= 90:
            tmp.append((i,0))
        if d[i][m-1] in key+'.$' or 97 <= ord(d[i][m-1]) <= 122:
            queue.append((i,m-1))
            visited[i][m-1] = 1
            u.append((i,m-1))
            if 97 <= ord(d[i][m-1]) <= 122:
                key += d[i][m-1].upper()
                d[i][m-1] = "."
        elif 65 <= ord(d[i][m-1]) <= 90:
            tmp.append((i,m-1))
    for j in range(m):
        if d[0][j] in key+'.$' or 97 <= ord(d[0][j]) <= 122:
            queue.append((0,j))
            visited[0][j] = 1
            u.append((0,j))
            if 97 <= ord(d[0][j]) <= 122:
                key += d[0][j].upper()
                d[0][j] = "."
        elif 65 <= ord(d[0][j]) <= 90:
            tmp.append((0,j))
        if d[n-1][j] in key+'.$' or 97 <= ord(d[n-1][j]) <= 122:
            queue.append((n-1,j))
            visited[n-1][j] = 1
            u.append((n-1,j))
            if 97 <= ord(d[n-1][j]) <= 122:
                key += d[n-1][j].upper()
                d[n-1][j] = "."
        elif 65 <= ord(d[n-1][j]) <= 90:
            tmp.append((n-1,j))
    start = queue[::]
    queue = deque(queue)
    
    while queue:
        x,y = queue.popleft()
        if d[x][y] == "$":
            d[x][y] = "."
            ans += 1
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if (d[nx][ny] == "." or d[nx][ny] in key) and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    u.append((nx,ny))
                elif 97 <= ord(d[nx][ny]) <= 122 and not visited[nx][ny]:
                    for kx,ky in u:
                        visited[kx][ky] = 0
                    u.clear()
                    key += d[nx][ny].upper()
                    queue = start[::]
                    for j,k in tmp:
                        if d[j][k] in key:
                            queue.append((j,k))
                            visited[j][k] = 1
                    d[nx][ny] = "."
                    queue.append((nx,ny))
                    queue = deque(queue)
                    u.append((nx,ny))
                elif d[nx][ny] == "$":
                    d[nx][ny] = "."
                    ans += 1
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    u.append((nx,ny))
    print(ans)