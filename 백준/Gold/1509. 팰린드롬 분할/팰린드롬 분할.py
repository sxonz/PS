s = input()
n = len(s)
dp = [[0]*(n+1) for i in range(n)]
for i in range(n):
    dp[i][0] = 1
    dp[i][1] = 1
for k in range(2,n+1):
    for i in range(k//2-(k%2^1),n-k//2):
        if dp[i-k//2+1+(k%2^1)][k-2] and s[i-k//2+(k%2^1)] == s[i+k//2]:
            dp[i-k//2+(k%2^1)][k] = 1

dist = [int(1e9)]*(n+1)
dist[0] = 0
for i in range(n):
    for j in range(n+1):
        if dp[i][j] and i+j <= n:
            dist[i+j] = min(dist[i+j],dist[i]+1)
print(dist[n])