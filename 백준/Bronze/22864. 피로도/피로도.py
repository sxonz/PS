a,b,c,m = map(int,input().split())
cur = 0
ans = 0
for i in range(24):
    if cur+a <= m:
        ans += b
        cur += a
    else:
        cur = max(cur-c,0)
print(ans)