n,m = map(int,input().split())
d = [int(input()) for i in range(n)]
for i in range(1,m+1):
    for j in range(n-1):
        if d[j]%i > d[j+1]%i:
            d[j],d[j+1] = d[j+1],d[j]
print(*d,sep='\n')