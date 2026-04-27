n = int(input())
d = []
maxv = -int(1e9)
minv = int(1e9)
for i,j in zip(map(int,input().split()),map(int,input().split())):
    maxv = max(maxv,i)
    minv = min(minv,i)
    d.append((i,j))
d.sort()

b = int(input())
l=1
r = maxv-minv+1
while l<r:
    mid = (l+r)//2
    e = -int(1e9)
    m = 0
    res = 0
    for i,c in d:
        if i > e:
            res += m
            m = int(1e7)
        m = min(m,c)
        e = i+mid
    if m < int(1e7):
        res += m
    if res <= b:
        r = mid
    else:
        l = mid+1
print(r)

