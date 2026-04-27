from math import ceil, log2
import sys
input = sys.stdin.readline
res = ["0","+","-"]
try:
    while True:
        n,q = map(int,input().split())
        d = [0] + list(map(int,input().split()))
        h = ceil(log2(n))+1
        segtree = [0]*int(pow(2,h))

        def build(l,r,idx):
            if l == r:
                s = d[l]
                segtree[idx] = s
                return s
            mid = (l+r)//2
            s = build(l,mid,idx*2) * build(mid+1,r,idx*2+1)
            if s == 0:
                segtree[idx] = 0
                return 0
            s //= abs(s)
            segtree[idx] = s
            return s
        
        build(1,n,1)

        def search(ql,qr,l,r,idx):
            if qr < l or r < ql:
                return 1
            if ql <= l and r <= qr:
                return segtree[idx]
            mid = (l+r)//2
            s = search(ql,qr,l,mid,idx*2) * search(ql,qr,mid+1,r,idx*2+1)
            if s == 0:
                return 0
            return s // abs(s)
        
        def update(qidx,v,l,r,idx):
            if qidx < l or r < qidx:
                return segtree[idx]
            if l == r:
                segtree[idx] = v
                return v
            mid = (l+r)//2
            s = update(qidx,v,l,mid,idx*2) * update(qidx,v,mid+1,r,idx*2+1)
            if s == 0:
                segtree[idx] = 0
                return 0
            s //= abs(s)
            segtree[idx] = s
            return s
        ans = ""
        for i in range(q):
            query,a,b = input().split()
            a,b = int(a),int(b)
            if query == "C":
                update(a,b,1,n,1)
            else:
                ans += res[search(a,b,1,n,1,)]
        print(ans)
except:
    pass