def solution(n, money):
    r = len(money)
    dp = [1]+[0]*n
    for i in money:
        for j in range(n+1):
            if j-i >= 0:
                dp[j] = (dp[j] + dp[j-i]) % 1000000007
    return dp[-1]