n,m = map(int,input().split())
edges = []
space = []
for _ in range(n):
    x,y = map(int,input().split())
    space.append((x,y))

for i in range(n):
    for j in range(i+1,n):
        edges.append(((((space[i][0]-space[j][0])**2+(space[i][1]-space[j][1])**2)**0.5),i,j))

edges.sort()

parent = [i for i in range(n)]

def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def cycle(a,b):
    return find(a) == find(b)

for _ in range(m):
    a,b = map(int,input().split())
    a-=1;b-=1
    union(a,b)

cost = 0
for c,a,b in edges:
    if not cycle(a,b):
        cost += c
        union(a,b)
res = str(round(cost*100)/100)
if res[-2] == ".":res += "0"
print(res)