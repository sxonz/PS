import sys
from math import *
input = sys.stdin.readline

MOD = 1000000007
n,m,k = map(int,input().split())
d = [0]+[int(input()) for i in range(n)]
h = ceil(log2(n))
size = int(pow(2,h+1))
segtree = [0]*size

def build(l,r,idx):
    if l == r:
        s = d[l]
        segtree[idx] = s
        return s
    mid = (l+r)//2
    s = build(l,mid,idx*2) * build(mid+1,r,idx*2+1) % MOD
    segtree[idx] = s
    return s

build(1,n,1)

def search(ql,qr,sl,sr,idx):
    if qr < sl or sr < ql:
        return 1
    if sl >= ql and sr <= qr:
        return segtree[idx]
    smid = (sl+sr)//2
    s = search(ql,qr,sl,smid,idx*2) * search(ql,qr,smid+1,sr,idx*2+1) % MOD
    return s

def update(i,v,sl,sr,idx):
    if i < sl or sr < i:
        return segtree[idx]
    if sl == sr:
        segtree[idx] = v
        return v
    smid = (sl+sr)//2
    s = update(i,v,sl,smid,idx*2) * update(i,v,smid+1,sr,idx*2+1) % MOD
    segtree[idx] = s
    return s

for i in range(m+k):
    q,a,b = map(int,input().split())
    if q == 1:
        update(a,b,1,n,1)
    else:
        print(search(a,b,1,n,1))