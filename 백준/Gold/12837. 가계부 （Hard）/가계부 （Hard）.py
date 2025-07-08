from math import log2, ceil

import sys
input = sys.stdin.readline
n,q = map(int,input().split())

h = ceil(log2(n)+1)
size = int(pow(2,h))
segtree = [0]*(size+1)

def search(ql,qr,l,r,idx):
    if qr < l or r < ql:
        return 0
    if ql <= l <= r <= qr:
        return segtree[idx]
    mid = (l+r)//2
    return search(ql,qr,l,mid,idx*2) + search(ql,qr,mid+1,r,idx*2+1)

def update(qidx,v,l,r,idx):
    if qidx < l or r < qidx:
        return segtree[idx]
    if l == r:
        segtree[idx] += v
        return segtree[idx]
    mid = (l+r)//2
    s = update(qidx,v,l,mid,idx*2) + update(qidx,v,mid+1,r,idx*2+1)
    segtree[idx] = s
    return s

for i in range(q):
    query,a,b = map(int,input().split())
    if query-1:
        print(search(a,b,1,n,1))
    else:
        update(a,b,1,n,1)
