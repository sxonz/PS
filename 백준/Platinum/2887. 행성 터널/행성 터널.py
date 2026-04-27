import sys
I = sys.stdin.readline
n = int(I())
p = []
xl = []
yl = []
zl = []
for i in range(n):
    x,y,z = map(int,I().split())
    p.append((x,y,z))
    xl.append((x,i))
    yl.append((y,i))
    zl.append((z,i))
xl.sort()
yl.sort()
zl.sort()
edges = []
for cur in xl,yl,zl:
    for i in range(1,n):
        edges.append((abs(cur[i][0]-cur[i-1][0]),cur[i-1][1],cur[i][1]))

edges.sort()

parent = [i for i in range(n)]

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
    return find(a) == find(b)
cost = 0
for c,a,b in edges:
    if not cycle(a,b):
        union(a,b)
        cost += c
print(cost)

