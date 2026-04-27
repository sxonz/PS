x,y,m = map(int,input().split())
d = [False]*(m+1)
d[0] = True
k = 0
for i in range(m+1):
    if d[i]:
        if i+x<=m:
            d[i+x] = True
            k = max(k,i+x)
        if i+y<=m:
            d[i+y] = True
            k = max(k,i+y)
print(k)
    