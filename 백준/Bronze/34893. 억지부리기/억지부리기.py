u,o,s = map(int,input().split())
bef = -1
cur = 0
ans = 0
for k in range(60,0,-1):
    if u-(1<<k) >= s+(1<<k-1):
        u -= 1<<k
        s += 1<<(k-1)
print(min(u,o,s))