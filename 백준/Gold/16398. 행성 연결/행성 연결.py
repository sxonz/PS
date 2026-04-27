n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i+1,n):
        edges.append((d[i][j],i,j))
edges.sort()
p = [i for i in range(n)]
def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        p[b] = p[a]
    else:
        p[a] = p[b]
def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]
def cycle(a,b):
    return find(a)==find(b)

cost = 0
for c,a,b in edges:
    if not cycle(a,b):
        union(a,b)
        cost += c
print(cost)