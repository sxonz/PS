import sys
I = sys.stdin.readline
v,e = map(int,I().split())
edges = []
for _ in range(e):
    a,b,c = map(int,I().split())
    edges.append((c,a,b))
edges.sort()

parent = [i for i in range(v+1)]

def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
def find(x):
    if parent[x] == x:return x
    parent[x] = find(parent[x])
    return parent[x]
def cycle(a,b):
    return find(a)==find(b)

lcost = 0
ans = 0
for c,a,b in edges:
    if not cycle(a,b):
        lcost = c
        union(a,b)
        ans += c
print(ans - lcost)
