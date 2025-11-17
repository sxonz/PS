import sys
sys.setrecursionlimit(10000)

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,l,r = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
day = 0
while True:
    flag = True
    group = [[i*n+j for j in range(n)] for i in range(n)]
    parents = list(range(n*n+1))
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a,b):
        a,b = find(a),find(b)
        if a<b:
            parents[b] = a
        else:
            parents[a] = b

    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0<=nx<n and 0<=ny<n:
                    if l <= abs(d[nx][ny]-d[i][j]) <= r:
                        flag = False
                        union(parents[group[nx][ny]],parents[group[i][j]])
    
    population = [0]*(n*n+1)
    border = [0]*(n*n+1)
    visited = [[False]*n for i in range(n)]
    def dfs(x,y):
        visited[x][y] = True
        population[find(group[x][y])] += d[x][y]
        border[find(group[x][y])] += 1
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                dfs(nx,ny)

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i,j)
    
    for i in range(n):
        for j in range(n):
            d[i][j] = population[find(group[i][j])] // border[find(group[i][j])]
    if flag:
        break
    day += 1
    
print(day)