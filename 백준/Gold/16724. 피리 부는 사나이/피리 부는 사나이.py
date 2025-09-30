import sys
sys.setrecursionlimit(200000)
dir = {"U":0,"D":1,"L":2,"R":3}
dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(input())for i in range(n)]

visited = [[False]*m for i in range(n)]

cnt = 0
cycle = []
def dfs(x,y):
    nx = x+dx[dir[d[x][y]]]
    ny = y+dy[dir[d[x][y]]]
    if not visited[nx][ny]:
        visited[nx][ny] = True
        cycle.append((nx,ny))
        f = dfs(nx,ny)
    else:
        f = (nx,ny) in cycle

    return f

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cycle = [(i,j)]
            visited[i][j] = True
            cnt += dfs(i,j)
print(cnt)