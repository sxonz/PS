from math import ceil,log2

n = int(input())
d = [0]+list(map(int,input().split()))

size = int(pow(2,ceil(log2(n))+1))
segtree = [(0,0)]*size

def build(l,r,idx):
    if l==r:
        segtree[idx] = (d[l],0)
        return segtree[idx]
    mid = (l+r)//2
    t = [*build(l,mid,idx*2),*build(mid+1,r,idx*2+1)]
    t.sort()
    segtree[idx] = (t[-1],t[-2])
    return segtree[idx]

def search(ql,qr,l,r,idx):
    if r<ql or qr<l:
        return (0,0)
    if ql<=l<=r<=qr:
        return segtree[idx]
    mid = (l+r)//2
    t = [*search(ql,qr,l,mid,idx*2),*search(ql,qr,mid+1,r,idx*2+1)]
    t.sort()
    return (t[-1],t[-2])

def update(qidx,qv,l,r,idx):
    if r<qidx or qidx<l:
        return segtree[idx]
    if l == r:
        segtree[idx] = (qv,0)
        return (qv,0)
    mid = (l+r)//2
    t = [*update(qidx,qv,l,mid,idx*2),*update(qidx,qv,mid+1,r,idx*2+1)]
    t.sort()
    segtree[idx] = (t[-1],t[-2])
    return segtree[idx]

build(1,n,1)
q = int(input())
for i in range(q):
    query,*tmp = map(int,input().split())
    if query == 1:
        update(*tmp,1,n,1)
    else:
        print(sum(search(*tmp,1,n,1)))
