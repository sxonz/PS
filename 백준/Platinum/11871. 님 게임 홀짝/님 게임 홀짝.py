n = int(input())
d = list(map(int,input().split()))
g = [-1 for _ in range(n)]
for i in range(n):
    if d[i] % 2 == 0:
        g[i] = d[i] // 2 - 1
    else:
        g[i] = d[i] // 2 + 1
res = 0
for i in g:
    res ^= i
if res == 0:
    print('cubelover')
else:
    print('koosaga')