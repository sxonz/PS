n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()

p1,p2 = 0,0
while p1<n and p2<m:
    if a[p1] < b[p2]:
        p1 += 1
    p2 += 1
print(sum(b[m-p1:]))