n = int(input())
d = list(map(int,input().split()))
d.sort()

M = 10000000000
a,b = 0,0
d.append(M)

ans = []
for i in range(n-1):
    s,e = i+1,n-1
    while s <= e:
        mid = (s+e)//2
        if abs(d[i]+d[mid]) > abs(d[i]+d[mid+1]):
            s = mid+1
        elif abs(d[i]+d[mid]) > abs(d[i]+d[mid-1]):
            e = mid-1
        else:
            break
    if abs(d[i]+d[mid]) < M:
        M = abs(d[i]+d[mid])
        ans = [d[i],d[mid]]
print(ans[0],ans[1])