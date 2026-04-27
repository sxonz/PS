n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

da = dict().fromkeys([0 for i in range(n + 1)], -1)
db = dict().fromkeys([0 for i in range(n + 1)], -1)

for i in range(n):
    da[a[i]] = i
    db[b[i]] = i

arr = []
for i in a:
    arr.append(db[i])

lis = []
bef = int(-1e10)

def lowerbound(s,e,k):
    while s<e:
        mid = (s+e)//2
        if lis[mid] >= k:
            e = mid
        elif lis[mid] < k:
            s = mid+1
    return e
l = 1
for i in range(len(arr)):
    if arr[i] > bef:
        lis.append(arr[i])
        bef = arr[i]
        l += 1
    else:
        tmp = lowerbound(0, l-1, arr[i])
        lis[tmp] = arr[i]
        bef = lis[-1]
print(len(lis))