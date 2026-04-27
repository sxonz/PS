from math import log2
n,k = map(int,input().split())
d = [2**i for i in range(24,-1,-1)]
idx = 0
m = 0
while k and n:
    if d[idx] <= n:
        k -= 1
        n -= d[idx]
        m = d[idx]
    if k == 0:
        break
    idx += 1
if k or not n:
    print(0)
else:
    print(m-n)