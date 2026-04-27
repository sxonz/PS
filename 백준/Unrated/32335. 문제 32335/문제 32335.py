n,m = map(int,input().split())
d = list(map(int,input()))
for i in range(n):
    if d[i] and 10-d[i] <= m:
        m -= 10-d[i]
        d[i] = 0
d[-1] = (d[-1]+m)%10
print(*d,sep='')
