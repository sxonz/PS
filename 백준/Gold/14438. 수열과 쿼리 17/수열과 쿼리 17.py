from math import ceil, log2
import sys
input = sys.stdin.readline
MAX = int(1e10)

n = int(input())
d = [0] + list(map(int,input().split()))
h = ceil(log2(n))+1
size = int(pow(2,h))
segtree = [0]*size

def build(l,r,idx):
    if l==r:
        s = d[l]
        segtree[idx] = s
        return s
    mid = (l+r)//2
    s = min(build(l,mid,idx*2), build(mid+1,r,idx*2+1))
    segtree[idx] = s
    return s

build(1,n,1)

def search(ql,qr,l,r,idx):
    if qr < l or r < ql:
        return MAX
    if ql <= l and r <= qr:
        return segtree[idx]
    mid = (l+r)//2
    return min(search(ql,qr,l,mid,idx*2), search(ql,qr,mid+1,r,idx*2+1))

def update(qidx,v,l,r,idx):
    if qidx < l or r < qidx:
        return segtree[idx]
    if l == r:
        segtree[idx] = v
        return v
    mid = (l+r)//2
    s = min(update(qidx,v,l,mid,idx*2), update(qidx,v,mid+1,r,idx*2+1))
    segtree[idx] = s
    return s

q = int(input())
for i in range(q):
    query,a,b = list(map(int,input().split()))
    if query == 1:
        update(a,b,1,n,1)
    else:
        print(search(a,b,1,n,1))


