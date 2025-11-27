n = int(input())
a = input()
d = [input() for i in range(n)]
dir = 0
dx = (1,0,-1,0)
dy = (0,1,0,-1)
ldx = (0,1,1,1,0,-1,-1,-1,0)
ldy = (0,-1,0,1,1,1,0,-1,-1)
def R(x):
    return (x+3)%4
def L(x):
    return (x+1)%4
def rev(x):
    return (x+2)%4

light = [[0]*n for i in range(n)]
z = []
for i in range(n):
    for j in range(n):
        if d[i][j] == "Z":
            z.append((i,j,0))

x,y = 0,0
for i in a:
    tmp = []
    for zx,zy,zdir in z:
        znx,zny = zx+dx[zdir], zy+dy[zdir]
        if 0<=znx<n and 0<=zny<n:
            tmp.append((znx,zny,zdir))
        else:
            tmp.append((zx,zy,rev(zdir)))
    if i == "F":
        nx,ny = x+dx[dir], y+dy[dir]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            nx,ny = x,y
        if d[nx][ny] == "S":
            for k in range(9):
                lnx,lny = nx+ldx[k], ny+ldy[k]
                if 0<=lnx<n and 0<=lny<n:
                    light[lnx][lny] = 1
    
    elif i == "R":
        dir = R(dir)
        nx,ny = x,y
    else:
        dir = L(dir)
        nx,ny = x,y
    x,y = nx,ny
    tmp2 = z[::]
    z = tmp[::]
    if light[x][y]:
        continue

    if (x,y,0) in tmp2 or (x,y,2) in tmp2 or (x,y,0) in tmp or (x,y,2) in tmp:
        print("Aaaaaah!")
        break
else:
    print("Phew...")
        

