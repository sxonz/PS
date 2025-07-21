from math import ceil, log2
import sys

input = sys.stdin.readline

n = int(input())
d = [0] + list(map(int,input().split()))
h = ceil(log2(n))+1
size = int(pow(2,h))
segtree = [0]*size
prop = [0]*size

def build(l,r,idx):
    if l == r:
        segtree[idx] = d[l]
        return d[l]
    mid = (l+r)//2
    segtree[idx] = build(l,mid,idx*2) ^ build(mid+1,r,idx*2+1)
    return segtree[idx]

build(1,n,1)

def propagation(l,r,idx):
    p = prop[idx]
    prop[idx] = 0
    if l == r:
        segtree[idx] ^= p
        return
    s = r-l+1
    if p:
        if s%2 == 1:
            segtree[idx] ^= p
    prop[idx*2] ^= p
    prop[idx*2+1] ^= p

def search(ql,qr,l,r,idx):
    propagation(l,r,idx)
    if qr < l or r < ql:
        return 0
    if ql <= l and r <= qr:
        return segtree[idx]
    mid = (l+r)//2
    s = search(ql,qr,l,mid,idx*2) ^ search(ql,qr,mid+1,r,idx*2+1)
    return s

def update(ql,qr,qv,l,r,idx):
    propagation(l,r,idx)

    if qr < l or r < ql:
        return segtree[idx]
    if ql <= l and r <= qr:
        s = r-l+1
        prop[idx] = qv
        if s%2 == 1:
            return segtree[idx] ^ qv
        return segtree[idx]
    mid = (l+r)//2
    s = update(ql,qr,qv,l,mid,idx*2) ^ update(ql,qr,qv,mid+1,r,idx*2+1)
    segtree[idx] = s
    return s

m = int(input())
for i in range(m):
    query = list(map(int,input().split()))
    query[1] += 1
    query[2] += 1
    if query[0] == 1:
        update(*query[1:],1,n,1)
    else:
        print(search(*query[1:],1,n,1))
        
