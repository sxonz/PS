I = lambda:map(int,input().split())
n,m = I()
edges = []
for _ in range(m):
    a,b,w = I()
    edges += [(-w,a,b)]
edges.sort()
p = list(range(n+1))
def F(x):
    if x-p[x]:p[x] = F(p[x])
    return p[x]

ans = int(1e10)
s,e = I()
for w,a,b in edges:
    a,b = F(a),F(b)
    if a-b:
        if a<b:
            p[b] = a
        else:
            p[a] = b
        ans = min(-w,ans)
        if F(s) == F(e):
            break
print(ans)