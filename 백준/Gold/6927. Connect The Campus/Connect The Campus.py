n = int(input())
d = []
for _ in range(n):
    d.append(tuple(map(int, input().split())))

edges = []
for i in range(n):
    for j in range(i + 1, n):
        edges.append((((d[i][0] - d[j][0]) ** 2 + (d[i][1] - d[j][1]) ** 2) ** 0.5, i, j))

edges.sort()
p = list(range(n + 1))

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

cost = 0
e = []
for c, a, b in edges:
    if find(a) != find(b):
        e += [(a + 1, b + 1)]
        union(a, b)
        cost += c

cost = "{:.2f}".format(round(cost, 2))
print(cost)
for i in e:
    print(*i)
