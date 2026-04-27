a,k = map(int,input().split())
dp = [0]*(k+1)
for i in range(a+1,k+1):
    dp[i] = (dp[i//2] * (R := (i%2 == 0 and i//2 >= a))) + ((R^1) * dp[i-1])+1
print(dp[k])