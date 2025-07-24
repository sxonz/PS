import sys
input = sys.stdin.readline
n,q = map(int,input().split())
d = []
for i in range(n):
    x1,x2,y = map(int,input().split())
    d.append((x1,x2,i+1))
d.sort()

parents = list(range(n+1))
def F(x):
    if x != parents[x]:parents[x] = F(parents[x])
    return parents[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b
last = d[0][1]
for i in range(1,n):
    if d[i][0] <= last:
        U(d[i-1][2],d[i][2])
    last = max(last,d[i][1])
    
for i in range(q):
    a,b = map(int,input().split())
    if F(a) == F(b):
        print(1)
    else:
        print(0)