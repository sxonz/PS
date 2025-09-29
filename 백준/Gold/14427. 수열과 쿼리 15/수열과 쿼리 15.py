from math import ceil,log2
import sys
input = sys.stdin.readline

n = int(input())
d = [0]+list(map(int,input().split()))

size = int(pow(2,ceil(log2(n)+1)))
segtree = [(int(1e20),-1)]*size

def build(l,r,idx):
    if l==r:
        segtree[idx] = (d[l],l)
        return (d[l],l)
    mid = (l+r)//2
    segtree[idx] = min(build(l,mid,idx*2), build(mid+1,r,idx*2+1))
    return segtree[idx]

def update(qidx,v,l,r,idx):
    if qidx < l or r < qidx:
        return segtree[idx]
    if l == r:
        segtree[idx] = (v,l)
        return (v,l)
    mid = (l+r)//2
    segtree[idx] = min(update(qidx,v,l,mid,idx*2), update(qidx,v,mid+1,r,idx*2+1))
    return segtree[idx]
    return s
build(1,n,1)
for i in range(int(input())):
    query,*d = map(int,input().split())
    if d:
        update(*d,1,n,1)
    else:
        print(segtree[1][1])
    
