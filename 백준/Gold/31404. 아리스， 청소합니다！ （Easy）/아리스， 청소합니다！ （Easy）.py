dx = (-1,0,1,0)
dy = (0,1,0,-1)

h,w = map(int,input().split())
x,y,dir = map(int,input().split())
a = [list(map(int,input())) for i in range(h)]
b = [list(map(int,input())) for i in range(h)]
board = [[1]*w for i in range(h)]

visited = [[[0,0,0,0] for j in range(w)] for i in range(h)]
r = [[[0,0,0,0] for j in range(w)] for i in range(h)]
used = []
last = 0
cur = 1
while True:
    if visited[x][y][dir] and r[x][y][dir]:
        print(last)
        break
    if board[x][y]:
        board[x][y] = 0
        last = cur
        dir = (dir + a[x][y])%4
        for t1,t2,t3 in used:
            r[t1][t2][t3] = 0
        used.clear()
    else:
        visited[x][y][dir] = 1
        r[x][y][dir] = 1
        used.append((x,y,dir))
        dir = (dir + b[x][y])%4
    x += dx[dir]
    y += dy[dir]
    if not (0<=x<h and 0<=y<w):
        print(last)
        break
    cur += 1
        
    