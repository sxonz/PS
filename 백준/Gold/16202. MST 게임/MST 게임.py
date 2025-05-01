ans = []
I=lambda:map(int,input().split())
n,m,k = I()
edges = []
for i in range(m):a,b = I();edges += [(i+1,a,b)]
for turn in range(k):
    p = list(range(n+1))
    def F(x):
        if x != p[x]:p[x] = F(p[x])
        return p[x]
    cost = 0
    for c,a,b in edges:
        if (a:=F(a)) != (b:=F(b)):p[a] = p[b] = min(a,b);cost += c
    if len(set([F(i) for i in range(1,n+1)])) != 1:cost = 0
    edges.pop(0)
    print(cost,end=' ')