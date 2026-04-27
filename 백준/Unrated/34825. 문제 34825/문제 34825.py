a,b = map(int,input().split())
c,d = map(int,input().split())

M = int(1e9)
x = (a+c)//2
y = (b+d)//2

dx = (-1,-1,-1,0,1,1,1,0,0)
dy = (-1,0,1,1,1,0,-1,-1,0)

for i in range(9):
    nx,ny = x+dx[i],y+dy[i]
    if -M <= nx <= M and -M <= ny <= M:
        if abs(a-nx) + abs(b-ny) == abs(c-nx) + abs(d-ny):
            print(nx,ny)
            break
else:
    print(-1)