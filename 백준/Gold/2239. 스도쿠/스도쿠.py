d = [list(map(int,input())) for i in range(9)]
hr = [[] for i in range(9)]
vt = [[] for i in range(9)]
bx = [[] for i in range(9)]

pos = []

for i in range(9):
    for j in range(9):
        if d[i][j]:
            hr[i].append(d[i][j])
            vt[j].append(d[i][j])
            bx[i//3*3+j//3].append(d[i][j])
        else:
            pos.append((i,j))
def back(idx,h,v,b,board):
    if idx == len(pos):
        for i in board:
            print(*i,sep='')
        exit()

    x,y = pos[idx]
    z = x//3*3+y//3
    r = set(h[x]+v[y]+b[z])

    for num in range(1,10):
        if num not in r:
            h[x].append(num)
            v[y].append(num)
            b[z].append(num)
            board[x][y] = num

            back(idx+1,h,v,b,board)

            board[x][y] = 0
            h[x].pop()
            v[y].pop()
            b[z].pop()
            
back(0,hr,vt,bx,d)