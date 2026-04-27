n,m,k = map(int,input().split())
lim = n-m
for i in range(1,k+1):
    if i > lim:
        print(1)
        continue
    res = 1
    a,b = n,n-m
    for j in range(i):
        res *= b/a
        b -= 1
        a -= 1
    print(1-res)
