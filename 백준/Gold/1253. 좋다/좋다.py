n = int(input())
d = list(map(int,input().split()))
d.sort()

def binSearch(idx1,idx2,x):
    l,r = 0,n
    while l<r:
        mid = (l+r)//2
        if d[mid] == x:
            if mid == idx1 or mid == idx2:
                if mid < n-1 and d[mid+1] > d[mid]:
                    r = mid
                else:
                    l = mid+1
            else:
                return True
        elif d[mid] < x:
            l = mid+1
        else:
            r = mid
    return False

cnt = 0
for i in range(n):
    for j in range(n):
        if i==j:continue
        if binSearch(i,j,d[i]-d[j]):
            cnt += 1
            break
print(cnt)
