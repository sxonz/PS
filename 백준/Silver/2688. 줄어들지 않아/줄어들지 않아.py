dp = [[0,0,0,0,0,0,0,0,0,0] for i in range(65)]
dp[1] = [1]*10
for i in range(2,65):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])
for i in range(int(input())):
    print(sum(dp[int(input())]))