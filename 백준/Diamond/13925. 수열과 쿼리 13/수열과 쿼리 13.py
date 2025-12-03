from math import log2,ceil
import sys
input = sys.stdin.readline

MOD = 1000000007

n = int(input())
d = [0] + list(map(int,input().split()))

size = int(pow(2,ceil(log2(n)+1)))
segtree = [0]*size

def build(l,r,idx):
    if l == r:
        segtree[idx] = d[l]
        return d[l]
    
    mid = (l+r)//2
    segtree[idx] = (build(l,mid,idx*2) + build(mid+1,r,idx*2+1)) % MOD
    return segtree[idx]

build(1,n,1)

prop = [[0,1] for i in range(size)]
def propagation(l,r,idx):
    addv,mulv = prop[idx]
    bound = r-l+1
    prop[idx] = [0,1]
    segtree[idx] = segtree[idx]*mulv%MOD
    segtree[idx] = (segtree[idx]+addv*bound)%MOD

    if l == r:
        return
    
    prop[idx*2] = [(prop[idx*2][0]*mulv+addv)%MOD, prop[idx*2][1]*mulv%MOD]
    prop[idx*2+1] = [(prop[idx*2+1][0]*mulv+addv)%MOD, prop[idx*2+1][1]*mulv%MOD]

def add(ql,qr,v,l,r,idx):
    propagation(l,r,idx)
    if qr<l or r<ql:
        return segtree[idx]
    
    if ql<=l and r<=qr:
        bound = r-l+1
        prop[idx][0] = v
        return segtree[idx] + v*bound
    
    mid = (l+r)//2
    segtree[idx] = (add(ql,qr,v,l,mid,idx*2) + add(ql,qr,v,mid+1,r,idx*2+1))%MOD
    return segtree[idx]

def mult(ql,qr,v,l,r,idx):
    propagation(l,r,idx)
    if qr<l or r<ql:
        return segtree[idx]
    if ql<=l and r<=qr:
        prop[idx][1] = v
        return segtree[idx]*v
    
    mid = (l+r)//2
    segtree[idx] = (mult(ql,qr,v,l,mid,idx*2) + mult(ql,qr,v,mid+1,r,idx*2+1))%MOD
    return segtree[idx]

def search(ql,qr,l,r,idx):
    propagation(l,r,idx)
    if qr<l or r<ql:
        return 0
    if ql<=l and r<=qr:
        return segtree[idx]
    
    mid = (l+r)//2
    return (search(ql,qr,l,mid,idx*2) + search(ql,qr,mid+1,r,idx*2+1))%MOD

q = int(input())
for i in range(q):
    query,*r = map(int,input().split())
    if query == 1:
        add(*r,1,n,1)
    elif query == 2:
        mult(*r,1,n,1)
    elif query == 3:
        mult(r[0],r[1],0,1,n,1)
        add(*r,1,n,1)
    else:
        print(search(*r,1,n,1))