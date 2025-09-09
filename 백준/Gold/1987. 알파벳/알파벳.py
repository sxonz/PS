dx = (-1,1,0,0)
dy = (0,0,-1,1)

r,c = map(int,input().split())
d = [input() for i in range(r)]
def back(x,y,path,depth):
    if depth == 26:
        return 26
    m = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            if d[nx][ny] not in path:
                m = max(m,back(nx,ny,path+d[nx][ny],1))
    return depth+m
print(back(0,0,d[0][0],1))