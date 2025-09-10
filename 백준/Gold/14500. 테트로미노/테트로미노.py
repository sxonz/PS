dx = (-1,0,1,0)
dy = (0,1,0,-1)
tetro = [[1,1,1],[1,2,3],[2,2,1],[2,1,2],[1,3,2],[2,2,3],[2,3,2],[1,3,0]]
inc = [(1,1,1),(1,1,1),(1,1,1),(1,1,1),(2,1,1),(1,1,1),(1,1,1),(2,1,1)]

n,m = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]

def Tet(block, depth,x,y):
    if depth == 4:
        return d[x][y]
    nx = x + dx[tetro[block][depth-1]] * inc[block][depth-1]
    ny = y + dy[tetro[block][depth-1]] * inc[block][depth-1]
    if 0<=nx<n and 0<=ny<m:
        return d[x][y] + Tet(block,depth+1,nx,ny)
    return -int(1e9)

def cw(n):
    return (n+1)%4

_max = -int(1e9)
for i in range(8):
    for j in range(4):
        for x in range(n):
            for y in range(m):
                if Tet(i,1,x,y) > _max:
                    _max = max(_max, Tet(i,1,x,y))
                    #print(_max,i,x,y,tetro[i])
        for k in range(3):
            tetro[i][k] = cw(tetro[i][k])
print(_max)

