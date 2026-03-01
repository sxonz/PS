n,k = map(int,input().split())
d = list(map(int,input().split()))

r = [0]*n
cur = 0
for i in range(n):
    cur = max(cur,d[i])
    r[i] = cur
    cur += k
for i in range(n-2,-1,-1):
    r[i] = r[i+1]-k
print(sum([i-j for i,j in zip(r,d)]))
