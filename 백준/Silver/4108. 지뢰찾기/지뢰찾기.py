dx = (-1,-1,-1,0,0,1,1,1)
dy = (-1,0,1,-1,1,-1,0,1)
while True:
    n,m = map(int,input().split())
    if (n,m) == (0,0):
        break
    d = [input() for i in range(n)]
    res = [["*"]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if d[i][j] == ".":
                tmp = 0
                for k in range(8):
                    nx,ny = i+dx[k],j+dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        if d[nx][ny] == "*":
                            tmp += 1
                res[i][j] = str(tmp)
    for i in res:
        print(''.join(i))