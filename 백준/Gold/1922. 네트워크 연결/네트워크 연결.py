import sys
I = input
n,m = int(I()),int(I())
edges = []
for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

parent = [i for i in range(n+1)]

def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
def find(x):
    if x == parent[x]:return x
    parent[x] = find(parent[x])
    return parent[x]
def cycle(a,b):
    return 0 if find(a)-find(b) else 1
ans = 0
for c,a,b in edges:
    if not cycle(a,b):
        union(a,b)
        ans += c
print(ans)