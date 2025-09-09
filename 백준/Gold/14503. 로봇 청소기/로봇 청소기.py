dx = (-1,0,1,0)
dy = (0,1,0,-1)

n,m = map(int,input().split())
r,c,dir = map(int,input().split())

d = [list(map(int,input().split())) for i in range(n)]
cleaned = [[False]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if d[i][j]:
            cleaned[i][j] = True

cl = 0
while 1:
    if not cleaned[r][c]:
        cleaned[r][c] = True
        cl += 1
    if 0 not in[cleaned[r+1][c],cleaned[r][c+1],cleaned[r-1][c],cleaned[r][c-1]]:
        if not d[r+dx[(dir+2)%4]][c+dy[(dir+2)%4]]:
            r += dx[(dir+2)%4]
            c += dy[(dir+2)%4]
            continue
        print(cl)
        break
    dir = (dir+3)%4
    if not cleaned[r+dx[dir]][c+dy[dir]]:
        r += dx[dir]
        c += dy[dir]