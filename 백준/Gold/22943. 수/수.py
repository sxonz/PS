from itertools import permutations

MAX = 98765

prime = []
p = [0]*MAX
for i in range(2,MAX):
    if not p[i]:
        prime.append(i)
        k = 2
        while i*k<MAX:
            p[i*k] = 1
            k += 1
primeadd = set()
primemult = set()

for i in range(len(prime)):
    for j in range(len(prime)):
        if i != j:
            primeadd.add(prime[i]+prime[j])
for i in range(len(prime)):
    for j in range(len(prime)):
        if prime[i]*prime[j] > MAX:
            break
        primemult.add(prime[i]*prime[j])
k,m = map(int,input().split())
res = 0
for i in permutations(range(10),k):
    if i[0] == 0:
        continue
    tmp = int(''.join([str(j) for j in i]))
    if tmp in primeadd:
        while tmp % m == 0:
            tmp //= m
        if tmp in primemult:
            res += 1

print(res)