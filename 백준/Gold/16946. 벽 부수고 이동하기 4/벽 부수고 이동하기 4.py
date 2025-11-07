import sys
sys.setrecursionlimit(1000000)

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [input() for i in range(n)]

group = [[0]*m for i in range(n)]
size = [0]
g = 1
visited = [[False]*m for i in range(n)]
def dfs(x,y):
    cur = 1
    group[x][y] = g
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and d[nx][ny] == "0":
                visited[nx][ny] = True
                cur += dfs(nx,ny)
    return cur

for i in range(n):
    for j in range(m):
        if d[i][j] == "0" and not visited[i][j]:
            visited[i][j] = True
            size.append(dfs(i,j))
            g += 1

for i in range(n):
    tmp = []
    for j in range(m):
        if d[i][j] == "0":
            tmp.append(0)
            continue
        use = set()
        for k in range(4):
            nx,ny = i+dx[k],j+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if d[nx][ny] == "0":
                    use.add((group[nx][ny],size[group[nx][ny]]))
        tmp.append((sum([i[1] for i in use])+1)%10)
    print(*tmp,sep='')

            