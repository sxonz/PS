n = 100000
d = [0]*(n+1)
while d[1] < n:
    cur = 1
    while cur<=n:
        d[cur] += 1
        cur += d[cur]
print(*d[1:])

