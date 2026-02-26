n,k,cur = map(int,input().split())
d = list(map(int,input().split()))
d.sort()
idx = 0
r = []
for i in range(k):
    while idx<n and d[idx] < cur:
        r.append(d[idx])
        idx += 1
    if r:
        cur += r.pop()
print(cur)