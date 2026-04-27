from collections import deque

dx = (-1,1,0,0)
dy = (0,0,-1,1)

n,m = map(int,input().split())
d = []
for i in range(n):
    d.append(list(map(int,input().split())))

queue = deque([])
visit = [[False]*m for _ in range(n)]
land = [[0]*m for _ in range(n)]
landnum = 1
for i in range(n):
    for j in range(m):
        if not visit[i][j] and d[i][j]:
            visit[i][j] = True
            land[i][j] = landnum
            queue.append((i,j))
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    nx,ny = x+dx[k],y+dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        if d[nx][ny] and not visit[nx][ny]:
                            visit[nx][ny] = True
                            queue.append((nx,ny))
                            land[nx][ny] = landnum
            landnum += 1
edges = []
distance = [[100]*landnum for _ in range(landnum)]

def dfs(sland,crange,pos,dir):
    x,y = pos
    nx,ny = x+dir[0],y+dir[1]
    if not (0<=nx<n and 0<=ny<m):
        return
    cur = land[nx][ny]
    if cur:
        if cur != sland and crange < distance[sland][cur] and crange > 1:
            distance[sland][cur] = crange
            edges.append((crange,sland,cur))
        return
    dfs(sland,crange+1,(nx,ny),dir)

for i in range(n):
    for j in range(m):
        if land[i][j]:
            for k in range(4):
                dfs(land[i][j],0,(i,j),(dx[k],dy[k]))
edges.sort()

parent = [i for i in range(landnum)]

def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def cycle(a,b):
    return find(a) == find(b)

cost = 0
for c,a,b in edges:
    if not cycle(a,b):
        cost += c
        union(a,b)

for i in range(1,landnum):
    find(i)

if len(set(parent[1:])) != 1:
    print(-1)
else:
    print(cost)