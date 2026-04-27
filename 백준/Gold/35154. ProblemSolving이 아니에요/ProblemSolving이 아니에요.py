n = 5001
dp = []
MOD = 998244353
for i in range(n):
    dp.append([0]*(i//2+2))
dp[0][0] = 1
l = [len(i) for i in dp]
for i in range(2,n):
    for j in range(i//2):
        dp[i][j] = dp[i-1][j+1]%MOD
    for j in range(1,i//2+1):
        dp[i][j] = (dp[i][j] + dp[i-2][j-1])%MOD
r = [sum(i)%MOD for i in dp]
input()
r[1] = -1
for t in list(map(int,input().split())):
    print(r[t])