n = int(input())
d = list(map(int,input().split()))
dp = [0]*n
def sis(x):
    if dp[x]:
        return dp[x]
    m = 1
    for i in range(x):
        if d[i] < d[x]:
            m += sis(i)
    m %= 998244353
    dp[x] = m
    return m
print(*[sis(i) for i in range(n)])
