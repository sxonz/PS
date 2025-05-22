n = int(input())
d = list(map(int, input().split()))

res = 0
def mergesort(l, r):
    global res
    if l == r:
        return

    mid = (l + r) // 2
    mergesort(l, mid)
    mergesort(mid + 1, r)

    p1, p2 = l, mid + 1
    tmp = []
    size = mid - l + 1
    while p1 <= mid and p2 <= r:
        if d[p1] <= d[p2]:
            tmp.append(d[p1])
            size -= 1
            p1 += 1
        else:
            res += size
            tmp.append(d[p2])
            p2 += 1
    while p1 <= mid:
        tmp.append(d[p1])
        p1 += 1
    while p2 <= r:
        tmp.append(d[p2])
        p2 += 1
    d[l:r+1] = tmp

mergesort(0, n - 1)
print(res)
