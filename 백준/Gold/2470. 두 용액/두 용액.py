n = int(input())
d = list(map(int,input().split()))
d.sort()
a,b = 0,0
M = int(1e10)
d.append(M)
for i in range(n-1):
    s,e = i+1,n-1
    while s<=e:
        mid = (s+e)//2
        if abs(d[i]+d[mid])>abs(d[i]+d[mid+1]):
            s = mid+1
        elif abs(d[i]+d[mid])>abs(d[i]+d[mid-1]):
            e = mid-1
        else:
            break
    if M > abs(d[i]+d[mid]):
        M = abs(d[i]+d[mid])
        a,b = d[i],d[mid]
print(a,b)