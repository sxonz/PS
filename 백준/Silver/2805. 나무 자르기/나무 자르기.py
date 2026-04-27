import sys
input=sys.stdin.readline

n,m = map(int,input().split())
woods = list(map(int,input().split()))

lo = 0
hi = max(woods)

while lo+1 < hi:
    mid = (lo+hi)//2

    temp = 0
    for i in woods:
        if i > mid:
            temp += (i-mid)

    if temp >= m:
        lo=mid
    
    else:
        hi=mid
print(lo)