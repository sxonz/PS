c,n = map(int,input().split())
h = [tuple(map(int,input().split())) for i in range(n)]
k = 0
d = dict()
for a,b in h:
    w = 1
    while b*w <= 1500:
        if a*w not in d:
            d[a*w] = b*w
            k += 1
        else:
            d[a*w] = max(d[a*w],b*w)
        w += 1
dp = [int(1e9)]*1501
dp[0] = 0
for a in d:
    for i in range(1500,d[a]-1,-1):
        dp[i] = min(dp[i],dp[i-d[a]]+a)
print(min(dp[c:]))