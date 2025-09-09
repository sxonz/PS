dx = (-1,0,1,0)
dy = (0,1,0,-1)
I = lambda:map(int,input().split())
n,m = I()
r,c,dir = I()

d = [list(I()) for i in range(n)]
cleaned = [i[::] for i in d]
cl = 0
while 1:
    if not cleaned[r][c]:
        cleaned[r][c] = True
        cl += 1
    if 0 not in[cleaned[r+1][c],cleaned[r][c+1],cleaned[r-1][c],cleaned[r][c-1]]:
        if not d[r+dx[x:=(dir+2)%4]][c+dy[x]]:
            r += dx[x]
            c += dy[x]
            continue
        print(cl)
        break
    dir = (dir+3)%4
    if not cleaned[r+dx[dir]][c+dy[dir]]:
        r += dx[dir]
        c += dy[dir]