n,m = map(int,input().split())
d = [int(input()) for i in range(m)]
d.sort()
maxv = 0
ans = 0
for i in range(m):
    if d[i]*min(m-i,n) > maxv:
        maxv = d[i]*min(m-i,n)
        ans = d[i]
print(ans,maxv)
        
    