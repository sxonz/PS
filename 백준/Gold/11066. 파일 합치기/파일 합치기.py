for t in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    dp = [[0]*n for i in range(n)]
    psum = [0]
    for i in d:
        psum.append(psum[-1]+i)
    def dnc(l,r):
        if l == r:
            return 0
        if l+1 == r:
            return d[l]+d[r]
        if dp[l][r]:
            return dp[l][r]
        tmp = int(1e12)
        for m in range(l,r):
            tmp = min(tmp,dnc(l,m)+dnc(m+1,r))
        tmp += psum[r+1]-psum[l]
        dp[l][r] = tmp
        return tmp
    print(dnc(0,n-1))
        
