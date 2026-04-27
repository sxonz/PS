n,m = map(int,input().split())
p = list(range(n+1))
def F(x):
    if x-p[x]:p[x] = F(p[x])
    return p[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
for i in range(m):
    a,b = map(int,input().split())
    U(a,b)
print(len(set([F(i) for i in range(1,n+1)]))-1)
