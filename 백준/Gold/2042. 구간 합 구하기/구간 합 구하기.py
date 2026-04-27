import sys
from math import *
n,m,k = map(int,input().split())
d = [0] + [int(input()) for i in range(n)]

h = ceil(log2(n))
size = int(pow(2,h+1))

segtree = [0]*size

def printsegtree():
    idx = 1
    for i in range(h+1):
        if idx >= size:
            break
        for j in range(1<<i):
            if idx >= size:
                break
            print(segtree[idx],end=' ')
            idx += 1
        print()

def build(idx,idxleft,idxright):
    if idxleft == idxright: 
        r = d[idxleft]
        segtree[idx] = r
        return r
    idxmid = (idxleft+idxright)//2
    r = build(idx*2,idxleft,idxmid) + build(idx*2+1,idxmid+1,idxright)
    segtree[idx] = r
    return r
    
build(1,1,n)

def search(querystart,queryend,idxleft,idxright,idx):
    if idxright < querystart or idxleft > queryend:
        return 0
    if idxleft >= querystart and idxright <= queryend:
        return segtree[idx]
    idxmid = (idxleft+idxright)//2
    r = search(querystart,queryend,idxleft,idxmid,idx*2) + search(querystart,queryend,idxmid+1,idxright,idx*2+1)
    return r
def update(queryidx,changed,idxleft,idxright,idx):
    if idxleft > queryidx or idxright < queryidx:
        return
    segtree[idx] += changed
    if idxleft == idxright:
        return
    idxmid = (idxleft+idxright)//2
    update(queryidx,changed,idxleft,idxmid,idx*2)
    update(queryidx,changed,idxmid+1,idxright,idx*2+1)
    return

for i in range(m+k):
    q,a,b = map(int,input().split())
    if q == 1:
        update(a,b-d[a],1,n,1)
        d[a] = b 
    else:
        print(search(a,b,1,n,1))
