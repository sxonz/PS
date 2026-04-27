n,p,q,x,y = map(int,input().split())
dp = {}

def dfs(v):
    if v <= 0:
        dp[v] = 1
        return 1
    elif v in dp:
        return dp[v]
    else:
        dp[v] = dfs(v//p-x) + dfs(v//q-y)
        return dp[v]

print(dfs(n))