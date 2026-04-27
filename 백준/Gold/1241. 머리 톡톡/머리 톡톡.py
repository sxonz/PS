n = int(input())
d = [int(input()) for _ in range(n)]
m = 1000001
res = [0]*m
h = [0]*101
for i in range(n):
    cur = d[i]
    if cur <= 100:
        h[cur] += 1
        continue
    k = d[i]
    while cur < m:
        res[cur] += 1
        cur += k
for i in range(n):
    tmp = res[d[i]]-1
    for j in range(1,101):
        if d[i] % j == 0:
            tmp += h[j]
    print(tmp)