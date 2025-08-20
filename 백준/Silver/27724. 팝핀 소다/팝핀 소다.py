from math import log2
n,m,k = map(int,input().split())
l = int(log2(n))
k -= 1
for i in range(l):
    r = int(pow(2,i))
    if k < r:
        break
    k -= r
else:
    i += 1
print(min(l,i+m))