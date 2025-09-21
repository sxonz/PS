n,a,b = map(int,input().split())
m = 0
cur = 0
d = list(map(int,input().split()))
for i in d:
    if i == a+cur*b:
        cur += 1
        m = max(cur,m)
print(m)