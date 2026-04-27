n = int(input())
m = int(input())
e = [[] for _ in range(n+1)]
f = [[] for _ in range(n+1)]
for i in range(m):
    x,a,b = input().split()
    a,b = int(a),int(b)
    if x == 'E':
        e[a].append(b)
        e[b].append(a)
    else:
        f[a].append(b)
        f[b].append(a)
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
for i in range(1,n+1):
    if len(e[i]) > 1:
        t = e[i][0]
        for k in e[i][1:]:
            if F(k)-F(t):
                U(k,t)
    for j in f[i]:
        if F(i)-F(j):
            U(i,j)
print(len(set([F(i) for i in range(1,n+1)])))
