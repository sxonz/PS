n = int(input())
d = list(map(int,input().split()))
d.sort()
def lowerbound(l,r,x):
    while l<r:
        mid = (l+r)//2
        if d[mid] < x:
            l = mid+1
        else:
            r = mid
    return r

ans = int(1e9)
for i in range(n):
    idx = lowerbound(i+1,n-1,-d[i])
    for k in idx-1,idx,idx+1:
        if 0<=k<n and k != i:
            ans = min(ans,d[k]+d[i],key=abs)
print(ans)