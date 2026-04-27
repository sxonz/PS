n,d=int(input()),(list(map(int,input().split()))+[0])[::-1]
dp=[0]*(n+1)
for i in range(1,n+1):dp[i] = min(dp[i-1]+1,d[i])
print(sum(dp))