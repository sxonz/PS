n,m = map(int,input().split())
MAX = 2000001
prime = [1]*MAX
prime[1] = 0
for i in range(2,MAX//2+1):
    if prime[i]:
        k = 2
        while i*k<MAX:
            prime[i*k] = 0
            k += 1

cur = 0
res = 0
dp = [0]*MAX
for i in range(1,MAX):
    if not prime[i]:
        if i-m<1:
            dp[i] = prime[i]^1
        else:
            dp[i] = dp[i-m] + 1
            cur = max(cur,dp[i])
            if dp[i] == n:
                res = i
                break
if cur<n:
    print(-1)
else:
    ans = []
    for i in range(n):
        ans.append(res)
        res -= m
    print(*ans[::-1])