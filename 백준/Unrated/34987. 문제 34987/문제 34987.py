n,m = map(int,input().split())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort()
b = [0]*(m+2)
idx = 0
ans = 0
cur = 0
for i in range(m+1):
    if idx == n:
        break
    cur -= b[m-i+1]
    while idx < n and d[idx][0] == i:
        if d[idx][1] <= m-i:
            b[d[idx][1]] += 1
            cur += 1
        idx += 1
    ans = max(cur,ans)
print(ans)