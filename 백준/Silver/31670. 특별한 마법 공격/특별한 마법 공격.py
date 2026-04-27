n = int(input())
d = list(map(int,input().split()))
if n == 1:
    print(0)
else:
    dp = [0]*(n+2)
    dp[2] = d[0] 
    dp[3] = d[1]
    for i in range(4,n+2):
        dp[i] = min(dp[i-2],dp[i-1])+d[i-2]
    print(min(dp[-1],dp[-2]))