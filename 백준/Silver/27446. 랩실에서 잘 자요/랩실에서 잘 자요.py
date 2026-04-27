n,m = map(int,input().split())
d = list(map(int,input().split()))
d = [i for i in range(1,n+1) if i not in d]
cur = 1
res = 0
for i in range(1,len(d)):
    if d[i] - d[i-1] < 4:
        cur += d[i]-d[i-1]
    else:
        res += 5 + cur*2
        cur = 1
if cur and d:
    res += 5 + cur*2
print(res)