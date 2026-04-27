n,m = map(int,input().split())
d = list(map(int,input().split()))
prefix = [d[0]]
for i in range(1,n):
    prefix.append(prefix[-1] + d[i])

result = 0
modulo = []
for i in prefix:
    modulo.append(i % m)
    if i % m == 0:
        result += 1

cnt = []
before = 0
cur = 0
for i in sorted(modulo):
    if i == before:
        cur += 1
    else:
        cnt.append(cur)
        cur = 1
    before = i
cnt.append(cur)

for i in cnt:
    tmp = 1
    for j in range(i-1,i+1):
        if j != 0:
            tmp *= j
    tmp = int(tmp/2)
    result += tmp
print(result)