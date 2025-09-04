MOD = 1000000007
MAX = 4000000

fact = [1] * (MAX + 1)
inv_fact = [1] * (MAX + 1)

for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[MAX] = pow(fact[MAX], MOD - 2, MOD)
for i in range(MAX - 1, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

inv_fact[0] = 1

def comb(n, r, MOD):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
n,k = map(int,input().split())
print(comb(n, k, MOD))
