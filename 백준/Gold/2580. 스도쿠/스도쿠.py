hr = [[] for i in range(9)]
vt = [[] for i in range(9)]
bx = [[] for i in range(9)]
zero = []
l = 0

d = [list(map(int,input().split())) for i in range(9)]

for i in range(9):
    for j in range(9):
        if d[i][j]:
            hr[i].append(d[i][j])
            vt[j].append(d[i][j])
            bx[i//3*3+j//3].append(d[i][j])
        else:
            zero.append((i,j))
            l += 1

def back(h,v,b,idx,board):
    if idx == l:
        for i in board:
            print(*i)
        exit(0)
    x,y = zero[idx]
    for i in range(1,10):
        if i not in h[x]+v[y]+b[x//3*3+y//3]:
            h[x].append(i)
            v[y].append(i)
            b[x//3*3+y//3].append(i)
            board[x][y] = i

            back(h,v,b,idx+1,board)   

            h[x].pop()
            v[y].pop()
            b[x//3*3+y//3].pop()
            board[x][y] = 0

back(hr,vt,bx,0,d)
