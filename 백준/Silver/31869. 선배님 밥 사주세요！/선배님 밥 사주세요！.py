n = int(input())
sunbu = {}
sunbumoney = {}
m = 0
for _ in range(n):
    s,d1,d2,cost = input().split()
    d1,d2,cost = int(d1),int(d2),int(cost)
    sunbu[s] = (d1*7+d2,cost)
    m = max(m,d1*7+d2)
for _ in range(n):
    s,money = input().split()
    sunbumoney[s] = int(money)
d = [0]*(m+1)
for s in sunbu:
    day,c = sunbu[s]
    if c <= sunbumoney[s]:
        d[day] = 1
cur = 0
_max = 0

for i in d:
    if i == 1:
        cur += 1
    else:
        _max = max(_max,cur)
        cur = 0
_max = max(_max,cur)
print(_max)