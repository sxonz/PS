from math import ceil,log2
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
d = [0]*(n+1)
h = ceil(log2(n))
size = int(pow(2,h+1))
segtree = [0]*size

def update(i,c,l,r,idx):
    if i<l or r<i:
        return segtree[idx]
    segtree[idx] += c
    s = segtree[idx]
    if l == r:
        return s
    mid = (l+r)//2
    update(i,c,l,mid,idx*2)
    update(i,c,mid+1,r,idx*2+1)
    return s
def search(ql,qr,l,r,idx):
    if qr < l or r < ql:
        return 0
    if ql <= l and r <= qr:
        return segtree[idx]
    mid = (l+r)//2
    return search(ql,qr,l,mid,idx*2) + search(ql,qr,mid+1,r,idx*2+1)

for i in range(m):
    query,a,b = map(int,input().split())
    if query:
        update(a,b-d[a],1,n,1)
        d[a] = b
    else:
        if a>b:
            a,b = b,a
        print(search(a,b,1,n,1))
