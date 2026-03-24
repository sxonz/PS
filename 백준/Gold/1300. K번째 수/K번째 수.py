n = int(input())
k = int(input())
l,r = 0,n*n+1
while l+1<r:
    mid = (l+r)//2
    tmp = 0
    for i in range(1,n+1):
        tmp += min(mid//i,n)
    if tmp >= k:
        r = mid
    else:
        l = mid
print(r)
