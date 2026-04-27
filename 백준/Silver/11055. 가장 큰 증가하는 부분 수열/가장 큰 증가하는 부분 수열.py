n = int(input())
d = list(map(int,input().split()))
dp = [0]*n
def big(x):
    if dp[x]:
        return dp[x]
    m = 0
    for i in range(x+1,n):
        if d[i] > d[x]:
            m = max(m,big(i))
    dp[x] = d[x] + m
    return dp[x]
for i in range(n):
    big(i)
print(max(dp))