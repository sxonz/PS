n = int(input())
d = list(map(int,input().split()))
m = int(1e10)
dp = [0]*n
for i in range(n):
    m = min(m,d[i])
    dp[i] = d[i] - m
print(max(dp))