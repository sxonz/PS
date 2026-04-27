n = int(input())

d = list(map(int,input().split()))

dp = [0]+[int(1e9)]*n

for i in range(n):

    for j in range(n-i):

        dp[i+j+1] = min(dp[i+j+1],dp[i]+d[j])

print(dp[n])