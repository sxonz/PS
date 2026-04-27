n,d,s,x=int(input()),list(map(int,input().split())),set(),int(1e9)
for i in range(n):
    for j in range(i+1,n):
        t=(d[j]-d[i])
        if t%(j-i):continue
        c=t//(j-i)
        r=d[i]-((i+1)*c)
        b=0
        for y in range(n):
            r+=c
            if d[y] != r:
                b+=1
        x=min(x,b)
print(x)
        