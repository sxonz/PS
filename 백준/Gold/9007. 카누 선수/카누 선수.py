for t in range(int(input())):
    w,n = map(int,input().split())
    d = [list(map(int,input().split())) for i in range(4)]
    a = []
    for i in d[0]:
        for j in d[1]:
            a.append(i+j)
    b = []
    for i in d[2]:
        for j in d[3]:
            b.append(i+j)
    
    l = len(a)
    a.append(-int(1e12))
    a.append(int(1e12))
    a.sort()
    b.sort(reverse=True)

    idx = 1
    ans = int(1e9)
    for i in b:
        while idx<=l and a[idx]+i < w:
            idx += 1
        ans = min(ans,a[idx-1]+i,a[idx]+i,key=lambda x:(abs(w-x),x))
    print(ans)