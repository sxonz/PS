I = lambda:int(input())
II = lambda:map(int,input().split())

for t in range(I()):
    n = I()
    d = list(II())
    r = dict()
    for i in d:
        if i not in r:
            r[i] = 0
        r[i] += 1
    d.sort()
    ans = set()
    for i in range(n):
        for j in range(i+1,n):
            if d[j]+d[j]-d[i] in r:
                ans.add((d[i],d[j]+d[j]+d[j]-d[i]))
    print(len(ans))