n = int(input())
d = [int(input()) for i in range(n)]
v = set(d)
ans = 0
for i in v:
    m = 0
    cur = 0
    bef = -1
    for j in d:
        if j == i:
            continue
        if j == bef:
            cur += 1
        else:
            cur = 1
        m = max(m,cur)
        bef = j
    ans = max(ans,m)
print(ans)