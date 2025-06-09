import sys
from math import ceil, log2
input = sys.stdin.readline

n = int(input())
d = [0]+list(map(int,input().split()))
h = ceil(log2(n))
size = int(pow(2,h+1))
segtree = [0]*size
prop = [0]*size

def build(l,r,idx):
    if l == r:
        s = d[l]
        segtree[idx] = s
        return s
    mid = (l+r)//2
    s = build(l,mid,idx*2) + build(mid+1,r,idx*2+1)
    segtree[idx] = s
    return s
build(1,n,1)

def propagation(l,r,idx):
    s = prop[idx]
    if s:
        segtree[idx] += s*(r-l+1)
        if l!=r:
            prop[idx*2] += s
            prop[idx*2+1] += s
        prop[idx] = 0

def search(qidx,l,r,idx):
    propagation(l,r,idx)
    if qidx < l or r < qidx:
        return 0
    if l == r:
        return segtree[idx]
    mid = (l+r)//2
    return search(qidx,l,mid,idx*2) + search(qidx,mid+1,r,idx*2+1)

def update(ql,qr,v,l,r,idx):
    propagation(l,r,idx)
    if r < ql or qr < l:
        return
    if ql <= l and r <= qr:
        segtree[idx] += v*(r-l+1)
        
        if l != r:
            prop[idx*2] += v
            prop[idx*2+1] += v
        return
    mid = (l+r)//2
    update(ql,qr,v,l,mid,idx*2)
    update(ql,qr,v,mid+1,r,idx*2+1)
    s = segtree[idx*2] + segtree[idx*2+1]
    segtree[idx] = s

m = int(input())
for i in range(m):
    t,*query = list(map(int,input().split()))
    if t == 1:
        update(*query,1,n,1)
    else:
        print(search(*query,1,n,1))