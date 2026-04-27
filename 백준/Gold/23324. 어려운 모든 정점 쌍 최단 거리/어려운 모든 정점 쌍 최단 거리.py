n,m,k = map(int,input().split())
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
s,e = 0,0
for i in range(1,m+1):
    a,b = map(int,input().split())
    if i == k:
        s,e = a,b
        continue
    if F(a)-F(b):
        U(a,b)
if F(s) == F(e):
    print(0)
else:
    p = [F(i) for i in range(n+1)]
    print(p.count(F(s)) * p.count(F(e)))