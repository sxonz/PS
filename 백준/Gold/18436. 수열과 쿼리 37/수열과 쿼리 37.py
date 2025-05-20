import sys
input = sys.stdin.readline
from math import ceil,log2

n = int(input())
d = [0] + list(map(int,input().split()))

h = ceil(log2(n))
size = int(pow(2,h+1))
seg = [0]*size

def build(l=1,r=n,idx=1):
    if l==r:
        s = d[l] % 2
        seg[idx] = s
        return s
    mid = (l+r)//2
    s = build(l,mid,idx*2) + build(mid+1,r,idx*2+1)
    seg[idx] = s
    return s

build()

def search(ql,qr,l=1,r=n,idx=1):
    if qr < l or r < ql:
        return 0
    if ql <= l and r <= qr:
        return seg[idx]
    mid = (l+r)//2
    return search(ql,qr,l,mid,idx*2) + search(ql,qr,mid+1,r,idx*2+1)

def update(i,c,l=1,r=n,idx=1):
    if i<l or r<i:
        return seg[idx]
    seg[idx] += c
    s = seg[idx]
    if l==r:
        return s
    mid = (l+r)//2
    update(i,c,l,mid,idx*2)
    update(i,c,mid+1,r,idx*2+1)


m = int(input())
for i in range(m):
    q,a,b = map(int,input().split())
    if q == 1:
        update(a,b%2-d[a]%2)
        d[a] = b
    elif q == 2:
        print(b-a+1-search(a,b))
    else:
        print(search(a,b))