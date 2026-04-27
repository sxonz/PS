from math import log2, ceil
import sys
input = sys.stdin.readline
NOT = 0.1

n,m,k = map(int,input().split())
d = [0] + [int(input()) for i in range(n)]

h = ceil(log2(n))
size = int(pow(2,h+1))
segtree = [0]*size
prop = [NOT] * size

def build(l,r,idx):
    if l == r:
        segtree[idx] = d[l]
        return segtree[idx]
    mid = (l+r)//2
    segtree[idx] = build(l,mid,idx*2) + build(mid+1,r,idx*2+1)
    return segtree[idx]

def propagation(l,r,idx):
    if prop[idx] == NOT:
        return
    segtree[idx] += prop[idx] * (r - l + 1)
    if l != r:
        if prop[idx*2] == NOT:
            prop[idx*2] = 0
        prop[idx*2] += prop[idx]
        if prop[idx*2+1] == NOT:
            prop[idx*2+1] = 0
        prop[idx*2+1] += prop[idx]
    prop[idx] = NOT

def update(ql,qr,qv,l,r,idx):
    propagation(l,r,idx)
    if qr < l or r < ql:
        return segtree[idx]
    if ql <= l and r <= qr:
        if prop[idx] == NOT:
            prop[idx] = 0
        prop[idx] += qv
        propagation(l,r,idx)
        return segtree[idx]
    mid = (l+r)//2
    segtree[idx] = update(ql,qr,qv,l,mid,idx*2) + update(ql,qr,qv,mid+1,r,idx*2+1)
    return segtree[idx]

def search(ql,qr,l,r,idx):
    propagation(l,r,idx)
    if qr < l or r < ql:
        return 0
    if ql <= l and r <= qr:
        return segtree[idx]
    mid = (l+r)//2
    return search(ql,qr,l,mid,idx*2) + search(ql,qr,mid+1,r,idx*2+1)

build(1,n,1)

for _ in range(m+k):
    query,a,b,*v = map(int,input().split())
    if query == 1:
        update(a,b,v[0],1,n,1)
    else:
        print(search(a,b,1,n,1))