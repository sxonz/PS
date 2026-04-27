import sys
input = sys.stdin.readline
while True:
    n,m = map(int,input().split())
    if n+m == 0:
        break
    edges = []
    full = 0
    for _ in range(m):
        a,b,c = map(int,input().split())
        full += c
        edges.append((c,a,b))
    edges.sort()
    parent = [i for i in range(n)]

    def union(a,b):
        a,b = find(a),find(b)
        if a<b:
            parent[b] = parent[a]
        else:
            parent[a] = parent[b]

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def cycle(a,b):
        return find(a) == find(b)

    cost = 0
    for c,a,b in edges:
        if not cycle(a,b):
            union(a,b)
            full -= c
            cost += c
    print(full)