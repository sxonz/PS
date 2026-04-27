import sys
input = sys.stdin.readline

n,r = map(int,input().split())
a = input().split()[0]
d = [(a,0)]
for i in range(n-1):
    name,dist = input().split()
    d.append((name,(d[-1][1]+r-int(dist))%r))
d.sort(key=lambda x:x[1])
d.append(("SUS",r))
res = []
for i in range(n):
    if d[i+1][1] - d[i][1] <= 1000:
        res.append(d[i][0])
res.sort()
if res:
    print(*res)
else:
    print(-1)