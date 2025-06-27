import sys
sys.setrecursionlimit(10000)
dx = (-1,1,0,0)
dy = (0,0,-1,1)
def solution(maps):
    n,m = len(maps), len(maps[0])
    visited = [[0]*m for i in range(n)]
    def dfs(x,y):
        cur = 0
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = 1
                    cur += dfs(nx,ny)
        return cur + int(maps[x][y])
    res = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = 1
                res.append(dfs(i,j))
    res.sort()
    return res or [-1]
        