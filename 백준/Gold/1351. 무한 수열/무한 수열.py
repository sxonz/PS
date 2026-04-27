n,p,q = map(int,input().split())
dp = {0:1}

def dfs(x):
    if x in dp:
        return dp[x]
    else:
        dp[x] = dfs(x//p) + dfs(x//q)
        return dp[x]

print(dfs(n))