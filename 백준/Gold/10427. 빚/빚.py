for t in range(int(input())):
    n,*d = map(int,input().split())
    d.sort()

    psum = [0]
    for i in d:
        psum.append(psum[-1]+i)

    res = 0
    for m in range(1,n+1):
        tmp = int(1e9)
        for i in range(1,n-m+2):
            tmp = min(tmp,d[i+m-2]*m-psum[i+m-1]+psum[i-1])
        res += tmp

    print(res)

