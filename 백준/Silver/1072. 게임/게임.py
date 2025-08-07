x,y=map(int,input().split()) 
z=(100*y)//x 
if z>=99:
    print(-1)
else: 
    l = 0
    r = x
    res = x
    while l<=r: 
        mid=(l+r)//2 
        if (100*(y+mid))//(x+mid)>z:
            res = mid
            r=mid-1 
        else: 
            l=mid+1
    print(res)