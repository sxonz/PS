n,m = map(int,input().split())
d = [0]*n
p = list(range(n))
def F(x):
    if x!=p[x]:
        p[x] = F(p[x])
    return p[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
for i in range(m):
    a,b = map(int,input().split())
    U(a-1,b-1)
    d[a-1] ^= 1
    d[b-1] ^= 1
print("YNEOS"[(d.count(1) not in [0,2] or len(set([F(i) for i in range(n)])) != 1)::2])
