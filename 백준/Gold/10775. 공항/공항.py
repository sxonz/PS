n,m = int(input()),int(input())
d = [int(input()) for i in range(m)]
p = list(range(n+1))
def F(x):
    if x-p[x]:
        p[x] = F(p[x])
    return p[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b
for i in range(m):
    if F(d[i]) == 0:
        break
    U(p[d[i]],p[d[i]]-1)
else:
    i+=1
print(i)