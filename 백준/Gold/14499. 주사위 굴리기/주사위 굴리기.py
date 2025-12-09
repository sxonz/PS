n,m,x,y,k = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]

dx = (0,0,0,-1,1)
dy = (0,1,-1,0,0)
cur = [0,0,0,0,0,0]
#상 하 북 남 서 동
def rotate(r):
    global cur
    if r == 1:
        cur = [cur[4],cur[5],cur[2],cur[3],cur[1],cur[0]]
    elif r == 2:
        cur = [cur[5],cur[4],cur[2],cur[3],cur[0],cur[1]]
    elif r == 3:
        cur = [cur[3],cur[2],cur[0],cur[1],cur[4],cur[5]]
    else:
        cur = [cur[2],cur[3],cur[1],cur[0],cur[4],cur[5]]

for i in list(map(int,input().split())):
    nx,ny = x+dx[i],y+dy[i]
    if 0<=nx<n and 0<=ny<m:
        x,y = nx,ny
        rotate(i)
        if not d[x][y]:
            d[x][y] = cur[1]
        else:
            cur[1] = d[x][y]
            d[x][y] = 0
        print(cur[0])