import sys
sys.setrecursionlimit(100000)

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = [list(input()) for i in range(n)]
group = [[0]*m for i in range(n)]
g = 1
cur = []
def dfs1(x,y):
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and not group[nx][ny] and d[nx][ny] == ".":
            group[nx][ny] = g
            cur.append((nx,ny))
            dfs1(nx,ny)

s = []
for i in range(n):
    for j in range(m):
        if d[i][j] == "L":
            d[i][j] = "."
            s += [(i,j)]
s1,s2 = s

for i in range(n):
    for j in range(m):
        if not group[i][j] and d[i][j] == ".":
            cur += [(i,j)]
            group[i][j] = g
            dfs1(i,j)
            g += 1

tmp = []
parents = list(range(g))
day = 0
def find(x):
    if parents[x]-x:
        parents[x] = find(parents[x])
    return parents[x]
def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b

def dfs2(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and d[nx][ny] == '.':
            if not group[nx][ny]:    
                tmp += [(nx,ny)]
                dfs2(nx,ny)
                group[nx][ny] = group[x][y]
            else:
                union(group[x][y],group[nx][ny])
while find(group[s1[0]][s1[1]]) != find(group[s2[0]][s2[1]]):
    for x,y in cur:
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not group[nx][ny]:
                    d[nx][ny] = '.'
                    tmp += [(nx,ny)]
                    group[nx][ny] = group[x][y]
                    dfs2(nx,ny)
                else:
                    union(group[x][y],group[nx][ny])

    cur = tmp[::]
    tmp.clear()
    day += 1
print(day)
