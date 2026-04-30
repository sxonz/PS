def solution(x, y, n):
    dp = [int(1e10)]*(y+1)
    dp[x] = 0
    for i in range(x,y):
        for next in (n,i,i*2):
            nx = i + next
            if nx <= y:
                dp[nx] = min(dp[nx],dp[i] + 1)
    return dp[y] if dp[y]-int(1e10) else -1