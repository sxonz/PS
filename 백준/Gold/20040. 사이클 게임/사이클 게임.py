n,m = map(int,input().split())

d = []
for _ in range(m):
    a,b = map(int,input().split())
    d.append((a,b))

parent = [i for i in range(n)]
def union(a,b):
    p_a,p_b = find(a),find(b)
    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

for i in range(m):
    a,b = d[i]
    if find(a) == find(b):
        print(i+1)
        break
    union(a,b)
else:
    print(0)