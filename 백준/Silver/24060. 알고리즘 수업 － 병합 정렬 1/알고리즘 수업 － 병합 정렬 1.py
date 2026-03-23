def merge_sort(l,r):
    if l < r:
        mid = (l+r)//2
        merge_sort(l,mid)
        merge_sort(mid+1,r)
        merge(l,mid,r)
def merge(l,mid,r):
    i = l
    j = mid+1
    tmp = []
    while i <= mid and j <= r:
        if d[i] <= d[j]:
            tmp.append(d[i])
            i += 1
        else:
            tmp.append(d[j])
            j += 1
    while i<=mid:
        tmp.append(d[i])
        i += 1
    while j<=r:
        tmp.append(d[j])
        j += 1

    for i in range(r-l+1):
        d[l+i] = tmp[i]
        ans.append(tmp[i])
n,k = map(int,input().split())
d = list(map(int,input().split()))
ans = []
merge_sort(0,n-1)
if k > len(ans):
    print(-1)
else:
    print(ans[k-1])