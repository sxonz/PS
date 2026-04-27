log = 18
root = 1
n = int(input())
ant = [0] + [int(input()) for _ in range(n)]
d = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    d[a] += [(b,c)]
    d[b] += [(a,c)]

depth = [0]*(n+1)
parents = [[root]*log for _ in range(n+1)]
distance = [[root]*log for _ in range(n+1)]

visited = [False]*(n+1)
visited[root] = True
def dfs(x):
    for nx,c in d[x]:
        if not visited[nx]:
            visited[nx] = True
            depth[nx] = depth[x] + 1
            parents[nx][0] = x
            distance[nx][0] = c
            dfs(nx)

dfs(root)

for k in range(1,log):
    for i in range(1,n+1):
        parents[i][k] = parents[parents[i][k-1]][k-1]
        distance[i][k] = distance[i][k-1] + distance[parents[i][k-1]][k-1]

def dist(x):
    energy = ant[x]
    for k in range(log-1,-1,-1):
        if energy >= distance[x][k]:
            energy -= distance[x][k]
            x = parents[x][k]
    return x

for i in range(1,n+1):
    print(dist(i))
