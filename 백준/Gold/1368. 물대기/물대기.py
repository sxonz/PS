from collections import deque

n = int(input())
water = [int(input()) for _ in range(n)]
d = [list(map(int, input().split())) for _ in range(n)]
edges = []

for i in range(n):
    edges.append((water[i], 0, i+1))
for i in range(n):
    for j in range(i+1, n):
        edges.append((d[i][j], i+1, j+1))
edges.sort()

p = [i for i in range(n+1)]

def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

cost = 0
used = []
graph = [[] for _ in range(n+1)]
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        graph[a].append(b)
        graph[b].append(a)
        used.append((c, a, b))
        cost += c
fin = cost
for c, a, b in used:
    tmp = cost - c
    nedges = edges.copy()
    nedges.remove((c, a, b))
    p = [i for i in range(n+1)]
    new = 0
    count = 0
    for nc, na, nb in nedges:
        if find(na) != find(nb):
            union(na, nb)
            new += nc
            count += 1
        if count == n:
            break
    
    tmp += new
    fin = min(fin, tmp)

print(fin)
