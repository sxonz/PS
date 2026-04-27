n = int(input())
d = list(map(int,input().split()))
dp = [0 for _ in range(n+1)]
dp[1] = 1

for i in range(2,n+1):
    temp = 0
    for j in range(1,i):
        if d[j-1] < d[i-1]:
            temp = max(temp,dp[j])
    dp[i] = temp + 1
print(max(dp))