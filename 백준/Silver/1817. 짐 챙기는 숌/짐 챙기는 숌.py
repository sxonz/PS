n,m = map(int,input().split())
if n:
    d = list(map(int,input().split()))
else:
    d = []
r = []
l = 0
for i in d:
    if r and r[-1]+i <= m:
        r[-1] += i
    else:
        r.append(i)
        l += 1
print(l)