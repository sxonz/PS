n,m = map(int,input().split())
d = list(map(int,input().split()))
mins = [int(1e7)]*(m+1)
maxs = [-int(1e7)]*(m+2)
for i in range(min(m+1,n)):
    mins[i] = min(mins[i-1],d[i])

for i in range(n-1,max(n-m-2,0),-1):
    maxs[n-i-1] = max(maxs[n-i],d[i])

r = -int(1e9)
for i in range(m+1):
    r = max(r,maxs[m-i]-mins[i])

print(r)