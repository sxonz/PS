from collections import deque
n,k = map(int,input().split())
d = list(map(int,input().split()))
c = d.count(1)
if k > c:
    print(-1)
    exit()
r = []
for i in range(n):
    if d[i] == 1:
        r.append(i)
ans = int(1e9)
for i in range(c-k+1):
    ans = min(ans,r[i+k-1]-r[i]+1)
print(ans)
