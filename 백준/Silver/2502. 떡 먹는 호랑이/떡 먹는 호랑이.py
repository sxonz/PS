n,k = map(int,input().split())
dp = [1,1] + [0]*(n-2)
while 1:
    for i in range(2,n):
        dp[i] = dp[i-1]+dp[i-2]
    if dp[n-1] == k:
        print(dp[0],dp[1],sep="\n")
        break
    elif dp[-1] > k:
        dp[0] += 1
        dp[1] = dp[0]
    else:
        dp[1] += 1