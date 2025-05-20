from math import ceil,log2
import sys
input = sys.stdin.readline

n,q = map(int,input().split())
d = [0]+list(map(int,input().split()))

h = ceil(log2(n))
size = int(pow(2,h+1))
segtree = [0]*size

def build(l,r,idx):
    if l==r:
        s = d[l]
        segtree[idx] = s
        return s
    mid = (l+r)//2
    s = build(l,mid,idx*2) + build(mid+1,r,idx*2+1)
    segtree[idx] = s
    return s

build(1,n,1)

def search(qa,qb,l,r,idx):
    if r<qa or qb<l:
        return 0
    if qa <= l and r <= qb:
        return segtree[idx]
    if l==r:
        return segtree[idx]
    mid = (l+r)//2
    return search(qa,qb,l,mid,idx*2) + search(qa,qb,mid+1,r,idx*2+1)

def update(i,c,l,r,idx):
    if i<l or r<i:
        return segtree[idx]
    segtree[idx] += c
    s = segtree[idx]
    if l==r:
        return s
    mid = (l+r)//2
    update(i,c,l,mid,idx*2)
    update(i,c,mid+1,r,idx*2+1)
    return s

for i in range(q):
    a,b,k,l = map(int,input().split())
    a,b = min(a,b),max(a,b)
    print(search(a,b,1,n,1))
    c = l-d[k]
    d[k] = l
    update(k,c,1,n,1)



