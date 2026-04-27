n,m = map(int,input().split())
d = list(map(int,input().split()))
s = sum(d)
l,r = max(d),s
while l<r:
    mid = tmp = (l+r)//2
    flag = False
    ray = 0
    for i in d:
        if i > tmp:
            tmp = mid
            ray += 1
            if ray == m:
                break
        tmp -= i
    else:
        flag = True
    if flag:
        r = mid
    else:
        l = mid+1
print(r)
