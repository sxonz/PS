n,e = map(int,input().split())
d = list(map(int,input().split()))
d.sort()
res = 1
bef = d[0]
for i in d:
    if i-bef >= e:
        res += 1
    bef = i
print(res)
