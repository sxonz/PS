n,m = map(int,input().split())
edges = []
for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

inf = int(1e9)
dist = [int(1e9)]*(n+1)
dist[1] = 0
for i in range(n-1):
    for a,b,c in edges:
        if dist[a] != inf:
            if dist[a]+c < dist[b]:
                dist[b] = dist[a]+c

no = 0
for a,b,c in edges:
    if dist[a] != inf:
        if dist[a]+c < dist[b]:
            no = 1

if no:
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i] == inf:
            print(-1)
        else:
            print(dist[i])


