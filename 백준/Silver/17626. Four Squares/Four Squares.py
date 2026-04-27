n = int(input())
dp = [5]*(n+1)
dp[0] = 0
squares = []
for i in range(1,int(n**0.5)+1):
    squares.append(i*i)
for i in range(n):
    for j in squares:
        if i+j > n:
            break
        dp[i+j] = min(dp[i+j],dp[i]+1)
print(dp[n])