I=lambda:map(int,input().split())
n,m = I()
s,e = I()
p = list(range(n))
distance = [0]*n
def F(x):
    if x-p[x]:p[x] = F(p[x])
    return p[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
edges = []
for i in range(m):
    a,b,w = I()
    edges += [(-w,a,b)]
edges.sort()
for w,a,b in edges:
    if F(a) != F(b):
        U(a,b)
        if F(s) == F(e):
            print(-w)
            break