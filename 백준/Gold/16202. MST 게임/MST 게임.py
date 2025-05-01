ans = []
n,m,k = map(int,input().split())
edges = []
for i in range(m):
    a,b = map(int,input().split())
    edges += [(i+1,a,b)]
for turn in range(k):
    p = list(range(n+1))
    def F(x):
        if x != p[x]:p[x] = F(p[x])
        return p[x]
    def U(a,b):
        a,b = F(a),F(b)
        if a<b:p[b] = a
        else:p[a] = b
    cost = 0
    for c,a,b in edges:
        if F(a) != F(b):U(a,b);cost += c
    if len(set([F(i) for i in range(1,n+1)])) != 1:cost = 0
    edges.pop(0)
    print(cost,end=' ')