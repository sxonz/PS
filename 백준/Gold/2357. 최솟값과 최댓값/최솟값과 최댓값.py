from math import *
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
d = [0] + [int(input()) for i in range(n)]
h = ceil(log2(n))
size = int(pow(2,h+1))
segtree = [(0,0)]*size

def build(l,r,idx):
    if l==r:
        x = d[l]
        segtree[idx] = (x,x)
        return (x,x)
    mid = (l+r)//2
    a = build(l,mid,idx*2)
    b = build(mid+1,r,idx*2+1)
    s = (min(a[0],b[0]),max(a[1],b[1]))
    segtree[idx] = s
    return s

build(1,n,1)

def search(ql,qr,ss,se,idx):
    if qr < ss or ql > se:
        return (int(1e11),-int(1e11))
    if ss >= ql and se <= qr:
        return segtree[idx]
    if ss == se:
        return segtree[idx]
    smid = (ss+se)//2
    a = search(ql,qr,ss,smid,idx*2)
    b = search(ql,qr,smid+1,se,idx*2+1)
    return (min(a[0],b[0]),max(a[1],b[1]))

for i in range(m):
    a,b = map(int,input().split())
    print(*search(a,b,1,n,1))