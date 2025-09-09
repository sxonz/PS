dx = (-1,0,1,0)
dy = (0,1,0,-1)

def rev(n):
    return (n+2)%4
def ccw(n):
    return (n+3)%4

n,m = map(int,input().split())
r,c,dir = map(int,input().split())

d = [list(map(int,input().split())) for i in range(n)]
cleaned = [[False]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if d[i][j]:
            cleaned[i][j] = True

cl = 0
while True:
    if not cleaned[r][c]:
        cleaned[r][c] = True
        cl += 1
    if [cleaned[r+1][c],cleaned[r][c+1],cleaned[r-1][c],cleaned[r][c-1]] == [1,1,1,1]:
        if not d[r+dx[rev(dir)]][c+dy[rev(dir)]]:
            r += dx[rev(dir)]
            c += dy[rev(dir)]
            continue
        print(cl)
        break
    dir = ccw(dir)
    if not cleaned[r+dx[dir]][c+dy[dir]]:
        r += dx[dir]
        c += dy[dir]