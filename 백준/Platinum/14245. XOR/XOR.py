from math import log2,ceil
import sys

input = sys.stdin.readline

n = int(input())
d = list(map(int,input().split()))
segtree = [0]*(size:=int(pow(2,ceil(log2(n)+1))))
prop = [0]*size

def build(l,r,idx):
    if l == r:
        segtree[idx] = d[l]
        return
    mid = (l+r)//2
    build(l,mid,idx*2)
    build(mid+1,r,idx*2+1)
    segtree[idx] = segtree[idx*2] + segtree[idx*2+1]

build(0,n-1,1)
def propagation(l,r,idx):
    p = prop[idx]
    if not p:
        return
    prop[idx] = 0
    if l == r:
        segtree[idx] ^= p
        return
    prop[idx*2] ^= p
    prop[idx*2+1] ^= p

def search(qidx,l,r,idx):
    propagation(l,r,idx)
    if l == r:
        return segtree[idx]
    mid = (l+r)//2
    if mid >= qidx:
        return search(qidx,l,mid,idx*2)
    return search(qidx,mid+1,r,idx*2+1)

def update(ql,qr,qv,l,r,idx):
    propagation(l,r,idx)
    if qr < l or r < ql:
        return segtree[idx]
    if ql <= l and r <= qr:
        prop[idx] = qv
        s = r-l+1
        return segtree[idx] ^ qv
    mid = (l+r)//2
    update(ql,qr,qv,l,mid,idx*2)
    update(ql,qr,qv,mid+1,r,idx*2+1)
    segtree[idx] = segtree[idx*2] ^ segtree[idx*2+1]
q = int(input())
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        update(*query[1:],0,n-1,1)
    else:
        print(search(query[1],0,n-1,1))