n = int(input())
edges = []
stars = []
for _ in range(n):
    x,y = map(float,input().split())
    stars.append((x,y))
for i in range(n):
    for j in range(i+1,n):
        edges.append((((stars[i][0]-stars[j][0])**2+(stars[i][1]-stars[j][1])**2)**0.5,i,j))
edges.sort()

parent = [i for i in range(n+1)]

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

res = 0
for c,a,b in edges:
    if not cycle(a,b):
        union(a,b)
        res += c
print(round(res*100)/100)