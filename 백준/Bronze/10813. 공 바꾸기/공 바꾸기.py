n,m = map(int,input().split())
d = list(range(1,n+1))
for i in range(m):
    a,b = map(int,input().split())
    d[a-1],d[b-1] = d[b-1],d[a-1]
print(*d)