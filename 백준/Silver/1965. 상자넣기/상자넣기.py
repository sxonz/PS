n = int(input())
d = list(map(int,input().split()))
lis = [0]
def lbound(x):
    l,r = 0,len(lis)-1
    while l<r:
        mid = (l+r)//2
        if lis[mid] < x:
            l = mid+1
        else:
            r = mid
    return r
for i in d:
    if i > lis[-1]:
        lis.append(i)
    else:
        idx = lbound(i)
        if i < lis[idx]:
            lis[idx] = i
print(len(lis)-1)