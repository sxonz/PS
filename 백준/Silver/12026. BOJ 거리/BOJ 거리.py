n = int(input())
s = input()
dp = [int(1e9)]*n
dp[0] = 0
f = {"B":"J", "O":"B", "J":"O"}
for i in range(1,n):
    idx = -1
    m = int(1e9)
    for j in range(i):
        if s[j] == f[s[i]]:
            if m > (i-j)**2 + dp[j]:
                m = (i-j)**2 + dp[j]
                idx = j
    if idx == -1:
        continue
    dp[i] = m
print(dp[n-1] if dp[n-1] != int(1e9) else -1)