from bisect import *
n = int(input())
t = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

dp = [0]*n
dp[0] = c[0]
for i in range(1,n):
    r = t[i]-b[i]
    idx = bisect_left(t,r,0,i)
    if not idx:
        dp[i] = max(dp[i-1],c[i])
    else:
        dp[i] = max(dp[i-1],dp[idx-1]+c[i])
print(dp[-1])