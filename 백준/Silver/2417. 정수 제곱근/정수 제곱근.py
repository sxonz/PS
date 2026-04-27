def check(q,n):
    return q**2>=n

num = int(input())

lo=-1
hi=num
while lo+1 < hi:
    mid = (lo+hi)//2

    if check(mid,num):
        hi=mid

    else:
        lo=mid

print(hi)