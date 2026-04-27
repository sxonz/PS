from bisect import *
n,c = map(int,input().split())
d = list(map(int,input().split()))
d.sort()
a = [0]
for i in range(n//2):
    tmp = []
    for j in a:
        tmp.append(j+d[i])
    for j in tmp:
        a.append(j)
a.sort()
b = [0]
for i in range(n//2,n):
    tmp = []
    for j in b:
        tmp.append(j+d[i])
    for j in tmp:
        b.append(j)
b = list(b)
b = [c-i for i in b if c-i>=0]
b.sort()
idx = 0
l = len(a)
ans = 0
for i in b:
    while idx<l and a[idx] <= i:
        idx += 1
    ans += idx
print(ans)