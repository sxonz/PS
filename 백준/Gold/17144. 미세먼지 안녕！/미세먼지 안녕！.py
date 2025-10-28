dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m,t = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
up = 0
for i in range(n):
    if d[i][0] == -1:
        up = i-1

for time in range(t):
    add = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if d[i][j] not in [-1,0]:
                c = 0
                for k in range(4):
                    nx,ny = i+dx[k], j+dy[k]
                    if 0<=nx<n and 0<=ny<m and d[nx][ny] != -1:
                        add[nx][ny] += d[i][j]//5
                        c += 1
                d[i][j] -= d[i][j]//5*c
    
    for i in range(n):
        for j in range(m):
            d[i][j] += add[i][j]
    
    dir = (0,3,1,2)
    z = 0
    bx,by,x,y = up,0,up-1,0
    for air in range(2):
        d[x][y] = 0
        while True:
            bx = x
            by = y
            x += dx[dir[z]]
            y += dy[dir[z]]
            if not air:
                if not (0<=x+dx[dir[z]]<=up and 0<=y+dy[dir[z]]<m):
                    z += 1
            else:
                if not (up<x+dx[dir[z]]<n and 0<=y+dy[dir[z]]<m):
                    z += 1
            if z == 4:
                d[bx][by] = 0
                break
            d[bx][by] = d[x][y]
        dir = (1,3,0,2)
        bx,by,x,y = up+1,0,up+2,0
        z = 0
ans = 0
for i in range(n):
    for j in range(m):
        if d[i][j] not in [-1,0]:
            ans += d[i][j]
print(ans)




