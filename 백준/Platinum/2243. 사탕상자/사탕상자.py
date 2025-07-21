from math import ceil, log2
import sys

input = sys.stdin.readline
n = 1000000
h = ceil(log2(n))+1
size = int(pow(2,h))
segtree = [0]*size

def search(qv,l,r,idx):
    segtree[idx] -= 1
    if l == r:
        return l
    mid = (l+r)//2
    if segtree[idx*2] >= qv:
        return search(qv,l,mid,idx*2)
    else:
        return search(qv-segtree[idx*2],mid+1,r,idx*2+1)

def update(qidx,qv,l,r,idx):
    if qidx < l or r < qidx:
        return segtree[idx]
    if l == r:
        segtree[idx] += qv
        return segtree[idx]
    mid = (l+r)//2
    s = update(qidx,qv,l,mid,idx*2) + update(qidx,qv,mid+1,r,idx*2+1)
    segtree[idx] = s
    return s

q = int(input())
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        print(search(query[1],1,n,1))
    else:
        update(*query[1:],1,n,1)
    