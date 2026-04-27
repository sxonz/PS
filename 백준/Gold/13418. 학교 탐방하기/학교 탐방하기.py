n,m = map(int,input().split())
edges = []
for _ in range(m+1):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()
p = list(range(n+1))
def union(a,b):
    a,b = find(a),find(b)
    if a<b:p[b] = a
    else:p[a] = b
def find(x):
    if x == p[x]:return x
    p[x] = find(p[x])
    return p[x]
def cycle(a,b):
    return find(a) == find(b)

cost = [0,0]
for c,a,b in edges:
    if not cycle(a,b):
        union(a,b)
        cost[0] += c^1
p = list(range(n+1))
edges.sort(reverse=True)
for c,a,b in edges:
    if not cycle(a,b):
        union(a,b)
        cost[1] += c^1
print(cost[0]**2 - cost[1]**2)