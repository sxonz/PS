for t in range(int(input())):
    n,k = map(int,input().split())
    l,r = 0,n//2+n%2
    flag = False

    while l<r:
        mid = (l+r)//2
        v = (n-mid) * (mid+1)
        if v == k:
            flag = True
            break
        if v < k:
            l = mid+1
        else:
            r = mid-1
    
    print("YES" if flag or (n-(l+r)//2) * ((l+r)//2+1)==k else "NO")
