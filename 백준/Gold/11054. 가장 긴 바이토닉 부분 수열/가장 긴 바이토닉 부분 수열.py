n = int(input())
d = list(map(int,input().split()))

ans = []

for _ in range(2):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    for i in range(2,n+1):
        temp = 0
        for j in range(1,i+1):
            if d[j-1] < d[i-1]:
                temp = max(temp,dp[j])
        dp[i] = temp + 1
    ans.append(dp)
    d.reverse()

ans[1].reverse()
ans[0] = ans[0][1:]
ans[1] = ans[1][:-1]
print(max([i+j for i,j in zip(ans[0],ans[1])])-1)