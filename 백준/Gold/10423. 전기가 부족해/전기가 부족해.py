n,m,k = map(int,input().split())
e = list(map(int,input().split()))
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

p = [i for i in range(n+1)]

def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
def find(x):
    if x == p[x]:return x
    p[x] = find(p[x])
    return p[x]
def cycle(a,b):
    return find(a)==find(b)

for elc in e[1:]:
    union(elc,e[0])

cost = 0
for c,a,b in edges:
    if not cycle(a,b):
        cost += c
        union(a,b)
print(cost)
