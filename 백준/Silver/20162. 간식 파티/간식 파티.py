n = int(input())
d = [int(input()) for i in range(n)]
lis = [0]*n
def s(idx):
    if lis[idx]:
        return lis[idx]
    m = 0
    for i in range(idx+1,n):
        if d[i] > d[idx]:
            m = max(m,s(i))
    lis[idx] = m + d[idx]
    return lis[idx]
print(max([s(i) for i in range(n)]))
