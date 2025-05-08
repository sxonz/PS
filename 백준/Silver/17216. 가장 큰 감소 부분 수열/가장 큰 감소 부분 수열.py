n = int(input())
d = list(map(int,input().split()))
dp = [0]*n
def lds(x):
    if dp[x]:
        return dp[x]
    m = 0
    for i in range(x+1,n):
        if d[i] < d[x]:
            m = max(m,lds(i))
    dp[x] = m + d[x]
    return dp[x]
print(max([lds(i) for i in range(n)]))