n,m = map(int,input().split())
d = [[0]*(m+2)]+[[0]+list(map(int,input().split()))+[0] for i in range(n)]+[[0]*(m+2)]

dx = (-1,1,0,0)
dy = (0,0,-1,1)
ans = n*m*2
for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(4):
            nx,ny = i+dx[k],j+dy[k]
            ans += max(0,d[i][j]-d[nx][ny])
print(ans)