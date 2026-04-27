n = int(input())
dp = {0 : 0, 1 : 0}
def pizza(x):
    if x in dp:return dp[x]
    if x%2:
        dp[x] = pizza(x//2) + pizza(x//2+1) + x//2*(x//2+1)
    else:
        dp[x] = pizza(x//2)*2 + (x//2)**2
    return dp[x]
    sus
print(pizza(n))