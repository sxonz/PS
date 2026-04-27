n,l,h,w = map(int,input().split())
a,b = 0,max(l,h,w)+1
while a+1<b:
    mid = (a+b)//2
    if (l//mid)*(h//mid)*(w//mid) >= n:
        a = mid
    else:
        b = mid
cur = 1
for i in range(11):
    cur /= 10
    for j in range(10):
        mid = a+cur
        if (l//mid)*(h//mid)*(w//mid) >= n:
            a += cur
print(a)