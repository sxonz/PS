n,m = map(int,input().split())
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges+=[(-c,a,b)]
edges.sort()
p=list(range(n+1))
def f(x):
    if x-p[x]:p[x] = f(p[x])
    return p[x]
def u(a,b):
    a,b=f(a),f(b)
    m=min(a,b)
    if a-b:p[a]=p[b]=m
cost = 0
for c,a,b in edges:
    if f(a)-f(b):
        u(a,b)
        cost += -c
for i in range(n+1):
    f(i)
print(cost if len(set(p[1:]))==1 else -1)