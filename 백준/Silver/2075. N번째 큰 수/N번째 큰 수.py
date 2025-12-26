n = int(input())
d = [list(map(int,input().split())) for i in range(n)]
idx = [n-1]*n
for _ in range(n):
    i,v = -1,-int(1e12)
    for j in range(n):
        if d[idx[j]][j] > v:
            i = j
            v = d[idx[j]][j]
    idx[i] -= 1
print(v)