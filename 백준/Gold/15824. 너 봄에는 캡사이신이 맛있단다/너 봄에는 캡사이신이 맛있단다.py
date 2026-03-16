n = int(input())
d = list(map(int,input().split()))
d.sort()
ans = 0
MOD = 1000000007
def power(x):
    if x <= 2:
        return 2**x
    elif x%2:
        return power(x//2)*power(x//2)*2%MOD
    else:
        return power(x//2)*power(x//2)%MOD
for i in range(n):
    ans = (ans+power(i)*d[i])%MOD
    ans = (ans-power(n-i-1)*d[i])%MOD
print(ans)