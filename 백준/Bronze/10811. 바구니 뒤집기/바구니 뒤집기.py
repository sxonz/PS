n,m = map(int,input().split())
d = list(range(1,n+1))
for i in range(m):
    a,b = map(int,input().split())
    tmp = d[:]
    for j,k in zip(range(a-1,b),reversed(range(a-1,b))):
        tmp[j] = d[k]
    d = tmp[:]
print(*d)