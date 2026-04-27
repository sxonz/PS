n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
k = 2
node = []
for i in range(n):
    for j in range(n):
        if board[i][j] in["K","S"]:
            board[i][j] = k
            node.append((k,i,j))
            k += 1
node.sort()
edges = []
flag = 0
for i in range(2,k):
    queue = [node[i-2][1:]]
    visit = [[False]*n for _ in range(n)]
    distance = [[0]*n for _ in range(n)]
    while queue:
        x,y = queue.pop(0)
        visit[x][y] = True
        for j,l in zip((-1,1,0,0),(0,0,-1,1)):
            nx,ny = x+j,y+l
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]and board[nx][ny] != "1":
                visit[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue+=[(nx,ny)]
    for num,x,y in node:
        if num-i:flag = not distance[x][y];edges += [(distance[x][y],i-2,num-2)]
edges.sort()

p = list(range(m+1))

def find(x):
    if x!=p[x]:p[x]=find(p[x])
    return p[x]
cost = 0
for c,a,b in edges:
    a,b=find(a),find(b);m=min(a,b)
    if a-b:p[a]=m;p[b]=m;cost+=c
print([cost,-1][int(flag)])