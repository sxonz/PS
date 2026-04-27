n,m = map(int,input().split())
d = [int(input()) for _ in range(n)]
p = [0]+[-i for i in d]
def F(x):
    if p[x]<0:
        return x
    p[x] = F(p[x])
    return p[x]
def U(a,b):
    f,g = F(a),F(b)
    if f<g:
        p[f] += p[g]
        p[g] = f
    else:
        p[g] += p[f]
        p[f] = g

ans = []
for i in range(m):
    a,b = map(int,input().split())
    if F(a)-F(b):
        U(a,b)
    ans.append(min(p[F(a)],p[F(b)]))
for i in ans:
    print(-i)