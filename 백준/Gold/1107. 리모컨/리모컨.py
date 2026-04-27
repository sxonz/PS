from itertools import product

n = int(input())
r = len(str(n))
m = int(input())
d = list(map(int,input().split())) if m else []
d = [str(i) for i in range(10) if i not in d]
res = int(1e9)
for i in product(d,repeat=r):
    if i:
        res = min(res,(abs(n-int(''.join(i)))))
for i in product(d,repeat=r-1):
    if i:
      res = min(res,(abs(n-int(''.join(i)))-1))
for i in product(d,repeat=r+1):
    res = min(res,(abs(n-int(''.join(i)))+1))
print(min(res+r,abs(100-n)))