from math import *
n = int(input())
ans = 1
MOD = int(pow(2,32))
prime = bytearray([1])*(n+1)
for i in range(2,n+1):
    if prime[i]:
        k = 2
        while i*k <= n:
            prime[i*k] = 0
            k += 1

        ans = ans*i**int(log(n,i))%MOD
print(ans)