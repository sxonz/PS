import sys
input = sys.stdin.readline
from bisect import *
from math import *

for t in range(int(input())):
    n = int(input())
    d = [tuple(map(int,input().split())) for i in range(n)]
    x = sorted([i[0] for i in d])
    y = sorted([i[1] for i in d])
    d = [(bisect_left(x,i[0]),bisect_right(y,i[1])) for i in d]
    d.sort(key=lambda x:(x[0],-x[1]))
    
    size = int(pow(2,ceil(log2(n)+1)))
    segtree = [0]*size
    def search(qx,l,r,idx):
        if r<qx:
            return 0
        if l>=qx:
            return segtree[idx]
        mid = (l+r)//2
        return search(qx,l,mid,idx*2)+search(qx,mid+1,r,idx*2+1)

    def update(qv,l,r,idx):
        if qv<l or r<qv:
            return segtree[idx]
        if l == r:
            segtree[idx] += 1
            return segtree[idx]
        mid = (l+r)//2
        segtree[idx] = update(qv,l,mid,idx*2)+update(qv,mid+1,r,idx*2+1)
        return segtree[idx]
    ans = 0
    for i in range(n):
        ans += search(d[i][1],1,n,1)
        update(d[i][1],1,n,1)
    print(ans)