def gcd(a, b):
    return b if not a%b else gcd(b,a%b)


n,s = map(int, input().split())
d = list(map(int, input().split()))

for i in range(n):
    d[i] = abs(s - d[i])
res = d[0]
for i in range(n):
    res = gcd(res, d[i])

print(res)