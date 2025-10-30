MOD = 1000000007
n = int(input())
dp = {0:0,1:1,2:1}

def fib(x):
    if x in dp:
        return dp[x]
    res = ((fib((x+1)//2) * fib((x+1)//2))%MOD)+((fib((x-1)//2)*fib((x-1)//2))%MOD)%MOD if x%2 else (fib(x//2)*(fib(x//2+1)+fib(x//2-1)))%MOD
    dp[x] = res%MOD
    return res%MOD

print(fib(n))