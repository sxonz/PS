import sys
from math import ceil,log2

input = sys.stdin.readline

n,q = map(int,input().split())

size = int(pow(2,ceil(log2(n)+1)))
segtree = [0]*size
prop = [0]*size

def propagation(l,r,idx):
    p = prop[idx]
    prop[idx] = 0
    p %= 2
    if not p:
        return
    segtree[idx] = r-l+1-segtree[idx]
    if l == r:
        return
    prop[idx*2] += 1
    prop[idx*2+1] += 1
    pass
def search(ql,qr,l,r,idx):
    propagation(l,r,idx)
    if qr<l or r<ql:
        return 0
    if ql <= l and r <= qr:
        return segtree[idx]
    
    mid = (l+r)//2
    return search(ql,qr,l,mid,idx*2) + search(ql,qr,mid+1,r,idx*2+1)
def update(ql,qr,l,r,idx):
    propagation(l,r,idx)
    if qr<l or r<ql:
        return segtree[idx]
    size = r-l+1
    if ql<=l and r<=qr:
        prop[idx] += 1
        return r-l+1-segtree[idx]
    mid = (l+r)//2
    segtree[idx] = update(ql,qr,l,mid,idx*2) + update(ql,qr,mid+1,r,idx*2+1)
    return segtree[idx]
    

for i in range(q):
    query,a,b = map(int,input().split())
    if query == 0:
        update(a,b,1,n,1)
    else:
        print(search(a,b,1,n,1))