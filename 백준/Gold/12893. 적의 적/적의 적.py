n,m = map(int,input().split())
d = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
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
flag = False
for i in range(1,n+1):
    if len(d[i]) > 1:
        t = d[i][0]
        for k in d[i][1:]:
            if F(k)-F(t):
                U(k,t)
            elif F(i) in [F(k),F(t)]:
                print(0)
                flag = True
                break
    if flag:
        break
else:
    print(1)