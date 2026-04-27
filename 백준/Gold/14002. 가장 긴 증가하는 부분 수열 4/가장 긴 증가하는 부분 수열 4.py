n = int(input())
d = list(map(int,input().split()))
dp = [0]*n
parent = [-1]*n

dp[0] = d[0]
for i in range(n):
    tmp = 0
    p = -1
    for j in range(i):
        if d[j] < d[i]:
            if dp[j] > tmp:
                p = j
                tmp = dp[j]
    dp[i] = tmp+1
    parent[i] = p
m = max(dp)
idx = dp.index(m)
ans = []
while parent[idx] != -1:
    ans.append(d[idx])
    idx = parent[idx]
ans.append(d[idx])
print(m)
print(*reversed(ans))