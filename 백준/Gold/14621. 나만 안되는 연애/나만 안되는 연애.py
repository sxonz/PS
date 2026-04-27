n,m = map(int,input().split())
g = input().split()
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1;b-=1
    if g[a] != g[b]:
        edges.append((c,a,b))
edges.sort()
p = [i for i in range(n)]
def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        p[b]=a
    else:
        p[a]=b
def find(x):
    if x==p[x]:return x
    p[x] = find(p[x])
    return p[x]
def cycle(a,b):
    return find(a)==find(b)

cost = 0
for c,a,b in edges:
    if not cycle(a,b):
        union(a,b)
        cost += c
for i in range(n):
    find(i)
if len(set(p)) == 1:
    print(cost)
else:
    print(-1)