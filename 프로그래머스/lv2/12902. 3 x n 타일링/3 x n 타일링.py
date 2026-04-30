def solution(n):
    dp = [1]+[0]*n
    for i in range(2,n+1,2):
        dp[i] = (sum(dp)*2 + dp[i-2])%1000000007
    return dp[n]
    