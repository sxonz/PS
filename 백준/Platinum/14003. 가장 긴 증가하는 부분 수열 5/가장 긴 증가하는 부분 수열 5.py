n = int(input())
d = list(map(int,input().split()))
lis = [(d[0],0)]
parent = [-1]*n

def lowerbound(x):
    s,e = 0,len(lis)-1
    while s<e:
        mid = (s+e)//2
        if lis[mid][0] >= x:
            e = mid
        else:
            s = mid + 1
    return e

for i in range(1,n):
    if d[i] > lis[-1][0]:
        parent[i] = lis[-1][1]
        lis.append((d[i],i))
        continue
    idx = lowerbound(d[i])
    lis[idx] = (d[i],i)
    if idx:
        parent[i] = lis[idx-1][1]

ans = []
w = lis[-1][1]
while w+1:
    ans.append(d[w])
    w = parent[w]
print(len(lis))
print(*ans[::-1])