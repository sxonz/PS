n = int(input())
dp = [[] for i in range(n+1)]
dp[1] = [1]
dp[2] = [2,1]
dp[3] = [2,3]
parents = [max(0,i-2) for i in range(n+1)]

for i in range(4,n+1):
    dp[i] = [dp[i-2][1]+2,dp[i-2][0]+2]

res = []
while n:
    res += dp[n]
    n = parents[n]
print("YES")
print(*res)