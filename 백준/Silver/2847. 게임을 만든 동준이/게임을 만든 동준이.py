n = int(input())
d = [int(input()) for i in range(n)]
cur = d[-1]
ans = 0
for i in range(n-1,-1,-1):
    if cur < d[i]:
        ans += d[i]-cur
    else:
        cur = d[i]
    cur -= 1
print(ans)