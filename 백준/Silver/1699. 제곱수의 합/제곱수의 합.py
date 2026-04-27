n = int(input())
dp = [0]+[5]*n
square = [i*i for i in range(1,int(n**0.5)+1)]
for i in range(n):
    for s in square:
        if i+s <= n:
            dp[i+s] = min(dp[i+s],dp[i]+1)
print(dp[n])