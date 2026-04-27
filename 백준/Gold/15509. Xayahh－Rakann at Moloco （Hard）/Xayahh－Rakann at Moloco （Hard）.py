import sys
I = lambda:map(int,sys.stdin.readline().split())
n,m,k = I()
n+=1
p = list(range(n))
def F(x):
    if x != p[x]:p[x] = F(p[x])
    return p[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:p[b] = a
    else:p[a] = b
for i in range(m):
    a,b = I()
    if F(a) != F(b):U(a,b)
r,l,s=[],0,set([0])
for i in set([F(i) for i in range(1,n)]):
    r.append(p.count(i));l += 1
flag = False
for i in range(l):
    for j in set(s):
        if j+r[i] not in s:
            s.add(j + r[i])
        if k in s:
            print("SAFE");flag = True;break
    if flag:break
else:print("DOOMED")        
