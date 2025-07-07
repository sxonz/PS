n = int(input())
hex = []
s = 0
for i in range(707):
    hex.append(s := s + i * 4 + 1)

dp = [10]*1000001
dp[0] = 0
for i in range(n+1):
    for j in hex:
        if i+j > n:
            hex.pop()
            break
        dp[i+j] = min(dp[i+j], dp[i] + 1)

print(dp[n])