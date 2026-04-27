import sys
input = sys.stdin.readline

n,m = map(int,input().split())
edges = []
for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

p = list(range(n+1))
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
def F(x):
    if x != p[x]:p[x] = F(p[x])
    return p[x]
mex = 1
for c,a,b in edges:
    if c != mex:
        print(mex)
        break
    if F(a) == F(b):
        print(mex)
        break
    if mex == n-1:
        print(n)
        break
    U(a,b)
    mex += 1