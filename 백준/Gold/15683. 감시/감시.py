dx = (1,0,-1,0)
dy = (0,1,0,-1)
dir = [0, [tuple([0]), tuple([1]), tuple([2]), tuple([3])], [(0,2),(1,3)], [(0,1),(1,2),(2,3),(3,0)], [(0,1,2),(1,2,3),(2,3,0),(3,0,1)], [(0,1,2,3)]]

n,m = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]


pos = []
w = 0
for i in range(n):
    for j in range(m):
        if d[i][j] == 0:
            w += 1
        elif d[i][j] < 6:
            pos.append((i,j))
l = len(pos)

ans = 0
def back(idx,board,cnt):
    if idx == l:
        return cnt
    cur = 0
    x,y =  pos[idx]
    num = board[x][y]

    for i in range(len(dir[num])):
        tmp = [j[::] for j in board]
        r = 0
        for j in dir[num][i]:
            nx,ny = x,y
            while 0<=nx<n and 0<=ny<m and tmp[nx][ny] != 6:
                if not tmp[nx][ny]:
                    tmp[nx][ny] = -1
                    r += 1
                nx += dx[j]
                ny += dy[j]
        cur = max(cur,back(idx+1,tmp,r))

    return cnt + cur

print(w - back(0,d,0))
    