MAX = 60
dp = [0]*MAX
dp[1] = 1
for i in range(2,MAX):
    dp[i] = dp[i-1] + dp[i-2] + 1

for t in range(int(input())):
    n = int(input())
    for i in range(MAX-1,-1,-1):
        if n >= dp[i]:
            print(i)
            break
