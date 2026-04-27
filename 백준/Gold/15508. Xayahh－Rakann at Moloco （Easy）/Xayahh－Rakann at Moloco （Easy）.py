from collections import deque
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
for i in range(m):
    a,b = map(int,input().split())
    if F(a)-F(b):U(a,b)
r = []
p = [F(i) for i in range(n+1)]
for i in set(p[1:]):
    r.append(p.count(i))
s = set([0])
l = len(r)
flag = False
for i in range(l):
    for j in set(s):
        if j+r[i] not in s:
            s.add(j + r[i])
        if k in s:
            print("SAFE")
            flag = True
            break
    if flag:
        break
else:
    print("DOOMED")        
