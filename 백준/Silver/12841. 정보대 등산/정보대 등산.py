n = int(input())
cross = list(map(int,input().split()))
l = list(map(int,input().split()))
r = list(map(int,input().split()))

minv = int(1e12)
ans = -1
cur = 0
rem = sum(r)
for i in range(n):
    if cur+rem+cross[i] < minv:
        minv = cur+rem+cross[i]
        ans = i+1
    if i<n-1:
        rem -= r[i]
        cur += l[i]
print(ans,minv)

