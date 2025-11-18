n = int(input())
d = list(map(int,input().split()))
d.sort()
ans = []
m = int(1e10)
for p1 in range(n-2):
    for p2 in range(p1+1,n-1):
        cur = d[p1] + d[p2]
        l,r = p2+1,n-1
        # d[p1] + d[p2] + d[r]이 0 이상인 최솟값일 때 r
        while l<r:
            mid = (l+r)//2
            if cur + d[mid] >= 0:
                r = mid
            else:
                l = mid+1
        if m > abs(cur + d[r]):
            m = abs(cur + d[r])
            ans = [p1,p2,r]
        if r-1 != p2 and m > abs(cur + d[r-1]):
            m = abs(cur + d[r-1])
            ans = [p1,p2,r-1]
print(*[d[i] for i in ans])
            