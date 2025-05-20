import sys
input = sys.stdin.readline
from math import ceil,log2

MIN = int(1e11)

n = int(input())
d = [0] + list(map(int,input().split()))

h = ceil(log2(n))
size = int(pow(2,h+1))
seg = [0]*size

def build(l,r,idx):
    if l == r:
        s = d[l]
        seg[idx] = (s,l)
        return (s,l)
    mid = (l+r)//2
    s = min(build(l,mid,idx*2), build(mid+1,r,idx*2+1))
    seg[idx] = s
    return s

build(1,n,1)

def search(ql,qr,l,r,idx):
    if r < ql or qr < l:
        return (MIN,MIN)
    if ql <= l and r <= qr:
        return seg[idx]
    mid = (l+r)//2
    return min(search(ql,qr,l,mid,idx*2),search(ql,qr,mid+1,r,idx*2+1))

def update(i,v,l,r,idx):
    if i<l or r<i:
        return seg[idx]
    if l == r:
        seg[idx] = (v,i)
        return (v,i)
    mid = (l+r)//2
    s = min(update(i,v,l,mid,idx*2),update(i,v,mid+1,r,idx*2+1))
    seg[idx] = s
    return s

m = int(input())
for i in range(m):
    q,a,b = map(int,input().split())
    if q == 1:
        update(a,b,1,n,1)
    else:
        print(search(a,b,1,n,1)[1])