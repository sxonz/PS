w,n = map(int,input().split())
d = list(map(int,input().split()))
ans = 0
r = set([d[0]+d[1]])
cur = [d[0],d[1]]
for i in range(2,n-1):
    for j in range(i+1,n):
        if w-d[i]-d[j] in r:
            ans = 1
    for j in cur:
        r.add(d[i]+j)
    cur.append(d[i])
print("YNEOS"[ans^1::2])
