n,q = map(int,input().split())
d = [[0]*(n+2) for i in range(6)]
dx = (-1,1,0,0,0)
dy = (0,0,-1,1,0)
for _ in range(q):
    query,*r = map(int,input().split())
    if query == 1:
        x,y = r
        for i in range(5):
            nx,ny = x+dx[i],y+dy[i]
            d[nx][ny] += 1
    else:
        fl = r[0]
        val,idx = -1,-1
        for i in range(n,0,-1):
            if d[fl][i] >= val:
                val = d[fl][i]
                idx = i
        print(idx)

val,x,y = -1,-1,-1
for i in 4,3,2,1:
    for j in range(n,0,-1):
        if d[i][j] >= val:
            val = d[i][j]
            x,y = i,j
print(x,y)
