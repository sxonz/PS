n = int(input())
d = [tuple((*map(int,input().split()),i)) for i in range(n)]
d.sort()
lis = [(0,-1)]
ran = 1
parent = [-1]*n
def lowerbound(l,r,x):
    while l<r:
        mid = (l+r)//2
        if lis[mid][0] < x:
            l = mid+1
        else:
            r = mid
    return r
for i in range(n):
    if d[i][1] > lis[-1][0]:
        parent[i] = lis[-1][1]
        lis.append((d[i][1],i))
        ran += 1
    else:
        idx = lowerbound(0,ran,d[i][1])
        if idx:
            parent[i] = lis[idx-1][1]
            lis[idx] = (d[i][1],i)

cur = lis[-1][1]
ans = set()
while cur != -1:
    ans.add(cur)
    cur = parent[cur]

print(n-len(ans))
for i in range(n):
    if i not in ans:
        print(d[i][0])