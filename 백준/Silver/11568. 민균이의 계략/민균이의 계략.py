n = int(input())
d = list(map(int,input().split()))
dp = [0]*n
def lis(x):
    if dp[x]:
        return dp[x]
    m = 0
    for i in range(x+1,n):
        if d[i] > d[x]:
            m = max(m,lis(i))
    dp[x] = m+1
    return m+1
print(max([lis(i) for i in range(n)]))