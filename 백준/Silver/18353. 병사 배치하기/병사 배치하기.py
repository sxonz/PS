import sys
sys.setrecursionlimit(3000)
n = int(input())
d = list(map(int,input().split()))
dp = [0]*(n)
def dec(x):
    if dp[x]:
        return dp[x]
    long = 0
    for i in range(x+1,n):
        if d[i] < d[x]:
            long = max(long,dec(i))
    dp[x] = long+1
    return dp[x]
for i in range(n):
    dec(i)
print(n-max(dp))