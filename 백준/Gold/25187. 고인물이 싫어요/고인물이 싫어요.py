import sys
I = lambda:map(int,sys.stdin.readline().split())
n,m,q = I()
d = list(I())
p = [[0,0]]+[[i+1,d[i]*2-1] for i in range(n)]
def F(x):
    if x-p[x][0]:p[x][0] = F(p[x][0])
    return p[x][0]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        p[b][0] = a
        p[a][1] += p[b][1]
        p[b][1] = 0
    else:
        p[a][0] = b
        p[b][1] += p[a][1]
        p[a][1] = 0
for i in range(m):
    a,b = I()
    if F(a)-F(b):
        U(a,b)
for i in range(q):
    query = int(input())
    print(int(p[F(query)][1] > 0))