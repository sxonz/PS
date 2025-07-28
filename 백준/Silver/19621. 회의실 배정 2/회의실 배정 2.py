n = int(input())
d = [0]+[list(map(int,input().split()))[2] for i in range(n)]


dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = max([0]+dp[:i-1]) + d[i]
print(max(dp))