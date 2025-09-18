I = lambda:map(int,input().split())
for test in range(int(input())):
    n = int(input())+2
    d = [tuple(I()) for i in range(n)]
    p = list(range(n))
    def Find(x):
        if x!=p[x]:
            p[x] = Find(p[x])
        return p[x]
    def Union(a,b):
        a,b = Find(a), Find(b)
        if a<b:
            p[b] = a
        else:
            p[a] = b

    for i in range(n-1):
        for j in range(i+1,n):
            if abs(d[i][0]-d[j][0]) + abs(d[i][1]-d[j][1]) <= 1000:
                Union(i,j)

    print("hsaapdp y"[Find(0) != Find(n-1)::2])
