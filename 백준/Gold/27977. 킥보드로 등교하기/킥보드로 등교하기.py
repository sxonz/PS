from bisect import *
l,n,k = map(int,input().split())
d = list(map(int,input().split()))
s,e = 0,l
while s<e:
    mid = (s+e)//2
    cur = 0
    for i in range(k):
        tmp = bisect_right(d,cur+mid)
        if tmp:
            cur = d[tmp-1]
    if cur+mid >= l:
        e = mid
    else:
        s = mid+1
print(e)